# Project for the third week of the course "MLOps: From Models to Production" 

A code repo for the project in week 3 for the [MLOps: From Models to Production](https://corise.com/course/mlops/) course.

## Getting Started

This projects was constructed using pipenv and docker.
You can run the api in two ways:

1. Run the server locally using:
```
    pip install pipenv
    pipenv install # install the Pipefile dependencies
    pipenv run uvicorn app.server:app --reload
    # Visit api docs: http://localhost:80/docs 
   
```
or

2. Running the api with Docker: Build the image and run the container
   ```bash
   docker build --platform linux/amd64 -t newsclassifier_api .
   docker run -p 80:80 newsclassifier_api 
   # Visit api docs: http://localhost:80/docs
   ```
   
3. Running using makefile<br>
   If you are on windows install [chocolatey](https://chocolatey.org/install) and [choco install make](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
   If you are a linux user, just use 
   ```make <action>```<br>
   After that you can use make <action> to build dockerfile, run dockerfile, test code and stop api.
   <br>
   The possible actions are:
   - make test: Run pytest in the code
   - make format: Format the code using Black and Isort. (Pylint is commented, but its possible too)
   - make build: Build the news-classifier image
   - make run: Start a named docker container (the name can be configured in makefile)
   - make exec: Open cli inside of the container
   - make stop: Stop the container
