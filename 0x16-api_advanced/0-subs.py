#!/usr/bin/python3
"""Function that queries Reddict API returns the number of subscribers
that is nonactive users, total subscribers for given subscription"""

import requests


def number_of_subscribers(subreddit):
    """return number of subscribers"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        results = response.json().get("data")
        return results.get("subscribers")
    else:
        return 0
