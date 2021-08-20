#!/usr/bin/python3
"""Paython script that fetches https://intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":

    html = requests.get('https://intranet.hbtn.io/status')
    html = html.text
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
