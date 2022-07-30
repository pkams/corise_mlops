# Here is simple Makefile that contains several make
# targets for building the Docker image and running
# the container.

# In addition there are other targets for entering
# a running container and stopping the container.

# To run a command, type 'make <target-name>' in a terminal
# where <target-name> is one of: 'build, 'run', 'exec', 'stop'
#
# The different actions are explained further in comments below.

format:
	pipenv run black .
	pipenv run isort .
# pipenv run pylint

test:
	pipenv run pytest

# ---
# We name the container so when we run it. We see this name
# when we enter the command: "docker ps" in a terminal
CONTAINER_NAME=news-classifier-container

#------
# Build the news-classifier image
# command in terminal: make build
build:
	docker build --platform linux/amd64 -t news-classifier .

#------
# Start a named docker container
# command in terminal: make run
run:
	docker run --name $(CONTAINER_NAME) --rm -p 80:80 news-classifier

#------
# Enter the running container. Use this command to enter the container and
# you can check the logs.out file.  Type command from a new terminal.
# command in new terminal: make exec
exec:
	docker exec -it $(CONTAINER_NAME) /bin/sh

#------
# Stop the container (notice we use the name of the container)
# command in new terminal: make stop
	docker stop $(CONTAINER_NAME)


# *** All credits to this Makefile are to Jerome from Corise MLOps Course ***