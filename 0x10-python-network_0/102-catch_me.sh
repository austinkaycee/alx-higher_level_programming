#!/bin/bash

# Send POST request with curl to cause the server to respond with "You got me!"
curl -X POST -H "Content-Type: application/json" -d '{"message": "You got me!"}' http://0.0.0.0:5000/catch_me

