#!/bin/bash
# takes in a URL, sends a GET request to the URL and displays the response
curl -s "$1" -X GET -L
