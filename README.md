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
