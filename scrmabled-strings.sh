#!/bin/bash
# Scrambled Word Count -Python (Docker:python:3.7-alpine)
#               author: Naresh Reddy M 

# Get the docker image for Scrambled application.
docker pull nareshreddymkt/python-scrambled-wc

# Run a container for the above docker image.

docker run -v $1:/code/files/dictionary_words -v $2:/code/files/search_string  -it nareshreddymkt/python-scrambled-wc
