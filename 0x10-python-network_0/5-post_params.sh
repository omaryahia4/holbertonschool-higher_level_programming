#!/bin/bash
# script that sends a POST request to the passed URL, and displays the body of the response.
curl -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" $1 -s
