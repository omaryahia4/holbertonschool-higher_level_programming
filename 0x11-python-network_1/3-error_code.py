#!/usr/bin/python3
""" manage urllib.error.HTTPError """
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
