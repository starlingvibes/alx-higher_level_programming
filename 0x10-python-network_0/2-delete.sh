#!/bin/bash
# sends a DELETE request to the URL passed as the first arg and displays the reponse
curl -s "$1" -X DELETE
