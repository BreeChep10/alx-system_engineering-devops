#!/usr/python3

import requests


def number_of_subscribers(subreddit):
    """
    function that returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        else:
            print("Subreddit data not found")
            return 0
    elif response.status_code == 404:
        print("Subreddit not found")
        return 0
    else:
        print("Error occurred while fetching subreddit data")
        return 0
