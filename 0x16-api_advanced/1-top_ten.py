#!/usr/bin/python3
"""
1-top_ten.py
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get('data')

    if not data:
        print(None)
        return

    children = data.get('children')

    if not children:
        print(None)
        return

    for i, child in enumerate(children):
        if i >= 10:
            break

        title = child.get('data').get('title')
        print(title)

