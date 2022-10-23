#!/bin/bash
# takes a URL, sends a request to that URL and displays the response size
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
