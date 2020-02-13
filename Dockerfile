FROM python:3.7-alpine
COPY . /code/
COPY * /code/
ENTRYPOINT [ "/bin/sh", "./code/scrmables_strings.sh" ]
