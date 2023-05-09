#!/usr/bin/python3
"""
Defines the number_of_subscribers function.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.

    Returns:
        The number of subscribers (not active users) of the subreddit,
        or 0 if the subreddit is invalid.
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    subscribers = data.get("subscribers", 0)

    return subscribers


