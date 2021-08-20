#!/usr/bin/python3
"""post request to the passed URL with the email as a parameter"""
import urllib.request
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(request) as response:
        email = response.read()
    print(email.decode('utf-8'))
