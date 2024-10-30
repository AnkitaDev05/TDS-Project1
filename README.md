# TDS Project 1

## Project Overview

- ### **Scraping the data** 
    This project scrapes GitHub users based in **Basel with more than 10 followers**. It collects user information and their repositories using the **GitHub API**. The results are saved as `users.csv` and `repositories.csv`.

- ### **Insights from analyzing the data**
    The Basel dataset is smaller, with fewer active contributors, suggesting a less active GitHub community than expected. This may be due to the city's small population and its focus on industries like pharmaceuticals and finance, which typically don't prioritize open-source software. Additionally, some users have many repositories but few followers.

- ### **An actionable recommendation based on analysis**
    Boost the frequency and diversity of tech meetups, hackathons, and workshops to encourage participation. Hosting training sessions focused on in-demand skills like AI/ML and cloud computing could benefit both new and experienced developers. Networking, collaboration, and community events can help users enhance their visibility.


## Data Scraping Process Overview  
- #### Generate and Use a Token:

    Created a **personal access token** from GitHub to authenticate API requests. This helps avoid rate limits for unauthenticated requests and ensures access to more data.

- #### Environment Setup:

    Used the **dotenv** library to manage environment variables securely. This prevents hardcoding sensitive information like API tokens in your script.

- #### Fetching Users:

    Utilized the **requests** library to make API calls. The script fetched users based in Basel with more than 10 followers by querying the GitHub API.

- #### Data Cleaning:

    Cleaned the data by standardizing or removing unnecessary fields (like Clean up company names). This ensures the dataset is consistent and relevant.

- #### Concurrency with ThreadPoolExecutor:

    Implemented **ThreadPoolExecutor** from the **concurrent.futures** module to fetch additional user details (like repositories) concurrently. This speeds up the data retrieval process by making multiple API calls at once.

- #### Data Storage:

    After gathering and cleaning the data, saved the results in **CSV format**. Created two files:
    - `users.csv` : Contains user details (username, location, followers, etc.).
    - `repositories.csv` : Lists the 500 most recently pushed repositories associated with each user.  


## **Data Analysis Process**   
The data analysis was conducted using **Python**, leveraging the following libraries:
- **Pandas**: Used for data manipulation and analysis, allowing for easy handling of CSV files and data cleaning.
- **scikit-learn (sklearn)**: Utilized for statistical analysis and modeling, helping to uncover patterns and relationships in the data.

