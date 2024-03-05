#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    """returning list of title of hot atricles"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": "after",
        "count": "count",
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    resultx = response.json().get("data")
    after = resultx.get("after")
    count += resultx.get("dist")

    for post in resultx.get("children"):
        hot_list.append(post.get("data").get("tittle"))


    if after is not None:
        return recurse(subreddit, hot_list, after)
    
    return hot_list
