#!/usr/bin/python3
"""
THIS SCRIPT Reddit API hot posts
"""

from requests import get


def top_ten(subreddit):
    """Get THE Titles of top 10 hot posts"""

    subreddit_info = get(
        "https://www.reddit.com/r/{:s}/hot.json?limit=9".format(subreddit),
        headers={"User-Agent": "Custom-User-Agent"},
        allow_redirects=False)

    if subreddit_info.status_code >= 300:
        print(None)
    else:
        for post in subreddit_info.json().get('data').get('children'):
            print(post.get('data').get('title'))


top_ten('programming')
