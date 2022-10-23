#!/bin/bash
# takes in a URL as an argument, sends a GET request and displays the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
