#!/usr/bin/python3
"""Python script that sends a POST request and displays the body of the response"""

import requests
from sys import argv
if __name__ == '__main__':
    email = {'email': argv[2]}
    response = requests.post(argv[1], data=email)
    print(response.text)
