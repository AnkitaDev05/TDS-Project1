import os
import requests
from concurrent.futures import ThreadPoolExecutor
from github import Github
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)
print(f"GITHUB_TOKEN: {GITHUB_TOKEN}")

def clean_company_name(company):
    if company:
        return company.strip().lstrip('@').upper()
    return company


def fetch_users():
    url = 'https://api.github.com/search/users'
    users_data = []
    page = 1

    while True:
        params = {
            'q': 'location:Basel followers:>10',  
            'per_page': 100,  
            'page': page
        }
        response = requests.get(url, headers={"Authorization": f"token {GITHUB_TOKEN}"}, params=params)
        data = response.json()

        if 'items' not in data or not data['items']:
            break  
        
        users_data.extend(data['items'])
        page += 1  

    return users_data


def fetch_user_details(user):
    user_data = []
    repo_data = []
    
    try:
        user_details = g.get_user(user['login'])

        company_cleaned = clean_company_name(user_details.company)

        user_data = [
            user_details.login,
            user_details.name,
            company_cleaned,
            user_details.location,
            user_details.email,
            user_details.hireable,
            user_details.bio,
            user_details.public_repos,
            user_details.followers,
            user_details.following,
            user_details.created_at
        ]


        repos = user_details.get_repos()
        for i, repo in enumerate(repos):
            if i >= 500:
                break  
            repo_data.append([
                user_details.login,
                repo.full_name,
                repo.created_at,
                repo.stargazers_count,
                repo.watchers_count,
                repo.language,
                repo.has_projects,
                repo.has_wiki,
                repo.license.name if repo.license else None
            ])
    
    except Exception as e:
        print(f"Error fetching data for {user['login']}: {e}")
    
    return user_data, repo_data


def main():

    users_data = fetch_users()
    
    user_list = []
    repo_list = []

    print(f"Fetched {len(users_data)} users.") 

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(fetch_user_details, users_data))

        for user_data, repo_data in results:
            if user_data:
                user_list.append(user_data)
            if repo_data:
                repo_list.extend(repo_data)

    print(f"Total users processed: {len(user_list)}")
    print(f"Total repositories processed: {len(repo_list)}")

    users_df = pd.DataFrame(user_list, columns=[
        'login', 'name', 'company', 'location', 'email', 'hireable', 
        'bio', 'public_repos', 'followers', 'following', 'created_at'])

    users_df.to_csv('users.csv', index=False)

    repos_df = pd.DataFrame(repo_list, columns=[
        'login', 'full_name', 'created_at', 'stargazers_count', 
        'watchers_count', 'language', 'has_projects', 'has_wiki', 'license_name'])

    repos_df.to_csv('repositories.csv', index=False)

    print("CSV files created successfully!")

if __name__ == "__main__":
    main()