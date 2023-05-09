#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.

    If the subreddit is invalid or not found, return 0.
    """

    # Set custom User-Agent header to avoid 429 error
    headers = {'User-Agent': 'Mozilla/5.0'}

    # Send HTTP GET request to Reddit API
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid
    if response.status_code != 200:
        return 0

    # Get the JSON data from the response and extract the subscriber count
    data = response.json()
    return data['data']['subscribers']

