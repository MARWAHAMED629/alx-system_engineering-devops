#!/usr/bin/python3
"""
Reddit API subscribers
"""

from requests import get


def number_of_subscribers(subreddit):
    """Get Number of subscribers"""

    subreddit_info = get(
        "https://www.reddit.com/r/{:s}/about.json".format(subreddit),
        headers={"User-Agent": "Custom-User-Agent"},
        allow_redirects=False)
     if subreddit_info.status_code >= 300
        return 0
    data = subreddit_info.json().get('data' , {})
            subscribers = data.get('subscribers', 0)
                return subscribers
