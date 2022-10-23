#!/bin/bash
# takes in a URL, sends a POST request and displays the response body
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
