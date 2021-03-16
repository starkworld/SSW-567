"""
HW04a: Github commits
Author: Nikhil Kalyan
Date: march 09, 2021
"""

import json
from typing import List
import requests


def get_user_repos(user_name: str) -> List:
    """This method returns list of repos that belongs to user
    Inputs: string
    Output: List
    """
    link: str = "https://api.github.com/users/" + user_name + "/repos"
    user_data = requests.get(link)
    repositories = json.loads(user_data.text)
    user_repos: List = []

    # Loop through nodes getting repository name, handle error of invalid username
    for repo in repositories:
        try:
            user_repos.append(repo.get("name"))
        except:
            user_repos = []

    return user_repos


def get_commit_counts(userName: str, repoName: str) -> int:
    """
    This function will return a count of how many commits an individual repo contents
    Inputs -  String, String
    Outputs - Integer
    """
    link = "https://api.github.com/repos/" + userName + "/" + repoName + "/commits"
    repoData = requests.get(link)
    commits = json.loads(repoData.text)
    commit_count = len(commits)
    return commit_count


# if __name__ == "__main__":
#     """
#     Main function that lists all the repos and lists each commit count given a specific
#     github user name.
#     """
#     userName: str = input("Enter Github username: ")
#     userRepos: List = get_user_repos(userName)
#
#     print("UserID: " + userName)
#
#     for repo in userRepos:
#         commitCount = get_commit_counts(userName, repo)
#         print("RepoName: " + repo + "and" + "Number of Commits: " + str(commitCount))
