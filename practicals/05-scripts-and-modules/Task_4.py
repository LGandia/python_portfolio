#!/usr/bin/env python3
import sys
import requests


def url_checker(link):
    try:
        url_response = requests.head(link)
        return url_response.status_code == 200

    except requests.ConnectionError:
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        if url_checker(url):
            print(f'{url} given valid')
        else:
            print(f'{url} is not valid')
    else:
        print('No url provided to be checked')
