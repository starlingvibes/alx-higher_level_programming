#!/bin/bash
# sends a JSON POST request to a URL passed as an arg, and displays the response body
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
