#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """print top ten hot post"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    post = {
            "limit": 10
            }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    result = response.json().get("data")
    [print(post.get("data").get("tittle"))for post in result.get("children")]
