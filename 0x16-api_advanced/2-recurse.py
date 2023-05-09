import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None

