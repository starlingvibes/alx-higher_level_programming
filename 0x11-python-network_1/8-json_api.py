#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
