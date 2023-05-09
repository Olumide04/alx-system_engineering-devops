import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100, "after": after}
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    for post in data["data"]["children"]:
        hot_list.append(post["data"]["title"])
    if data["data"]["after"] is not None:
        recurse(subreddit, hot_list, data["data"]["after"])
    return hot_list

