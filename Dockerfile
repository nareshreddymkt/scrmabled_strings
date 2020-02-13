FROM python:3.7-alpine
COPY scrmabled_* /code/
ENTRYPOINT [ "/bin/sh", "./code/scrmabled_strings.sh" ]
