#!/usr/bin/python3
"""
Reddit API subscribers
"""

from requests import get
from requests.exceptions import RequestException  # Import for exception handling


def number_of_subscribers(subreddit):
    """
    Get Number of subscribers for a subreddit.

    Args:
        subreddit: The name of the subreddit to query.

    Returns:
        The number of subscribers for the subreddit, or None if an error occurs.
    """

    subreddit_info = get(
        "https://www.reddit.com/r/{:s}/about.json".format(subreddit),
        headers={"User-Agent": "Custom-User-Agent"},
        allow_redirects=False,
    )

    try:
        # Check for successful request (status code < 300)
        subreddit_info.raise_for_status()  # Raise an exception for non-2xx codes
        # Extract subscriber count if successful
        return subreddit_info.json().get("data", {}).get("subscribers")
    except RequestException as e:
        # Handle any request exceptions
        print(f"An error occurred: {e}")
        return None  # Return None on error


if __name__ == "__main__":
    # Example usage
    subreddit_name = "learnpython"  # Replace with your desired subreddit
    subscribers = number_of_subscribers(subreddit_name)

    if subscribers is not None:
        print(f"The subreddit '{subreddit_name}' has {subscribers} subscribers.")
    else:
        print(f"An error occurred while retrieving subscriber count for '{subreddit_name}'.")
