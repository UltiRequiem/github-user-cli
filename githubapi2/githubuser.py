import sys

import requests

GITHUB_API = "https://api.github.com"


def get_username():
    return str(input("Username: "))


def get_user_details(username):
    return requests.get(f"{GITHUB_API}/users/{username}").json()


def get_important_data(user_details):
    return {
        "username": user_details["login"],
        "id": user_details["id"],
        "name": user_details["name"],
        "company": user_details["company"],
        "webpage": user_details["blog"],
        "location": user_details["location"],
        "bio": user_details["bio"],
        "twitter_username": user_details["twitter_username"],
        "total_public_repos": user_details["public_repos"],
        "total_public_gists": user_details["public_gists"],
        "total_followers": user_details["followers"],
        "total_following": user_details["following"],
        "created_date": user_details["created_at"],
    }


def print_user_data(data):
    print(f"{data['name']}: {data['bio']}")
    print(
        f"Location: {data['location']} | Twitter Username: {data['twitter_username']} | Web Page: https://{data['webpage']}"
    )
    print(
        f"Total Public Repositories: {data['total_public_repos']} | Total Public Gists {data['total_public_gists']} | Total Followers: {data['total_followers']} | Total Following: {data['total_following']}"
    )


def run():
    user_details = get_user_details(get_username())
    important_data = get_important_data(user_details)
    print_user_data(important_data)


if __name__ == "__main__":
    run()
