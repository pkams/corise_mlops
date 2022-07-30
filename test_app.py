import os

import pytest
from fastapi.testclient import TestClient

from .app.server import app

os.chdir("app")
client = TestClient(app)

""" 
This part is optional. 

We've built our web application, and containerized it with Docker.
But imagine a team of ML engineers and scientists that needs to maintain, improve and scale this service over time. 
It would be nice to write some tests to ensure we don't regress! 

  1. `Pytest` is a popular testing framework for Python. If you haven't used it before, take a look at https://docs.pytest.org/en/7.1.x/getting-started.html to get started and familiarize yourself with this library.
   
  2. How do we test FastAPI applications with Pytest? Glad you asked, here's two resources to help you get started:
    (i) Introduction to testing FastAPI: https://fastapi.tiangolo.com/tutorial/testing/
    (ii) Testing FastAPI with startup and shutdown events: https://fastapi.tiangolo.com/advanced/testing-events/

"""


def test_root():
    """
    [TO BE IMPLEMENTED]
    Test the root ("/") endpoint, which just returns a {"Hello": "World"} json response
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_predict_empty():
    """
    [TO BE IMPLEMENTED]
    Test the "/predict" endpoint, with an empty request body
    """
    response = client.post("/predict", json={})
    assert response.status_code == 422


def test_predict_en_lang():
    """
    [TO BE IMPLEMENTED]
    Test the "/predict" endpoint, with an input text in English (you can use one of the test cases provided in README.md)
    """
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "source": "BBC Technology",
                "url": "http://news.bbc.co.uk/go/click/rss/0.91/public/-/2/hi/business/4144939.stm",
                "title": "System gremlins resolved at HSBC",
                "description": "Computer glitches which led to chaos for HSBC customers on Monday are fixed, the High Street bank confirms.",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "scores": pytest.approx(
                {
                    "Business": 0.24155971796626052,
                    "Entertainment": 0.2859147950447055,
                    "Health": 0.05094225507018263,
                    "Music Feeds": 0.0047951969215028825,
                    "Sci/Tech": 0.31764412982445556,
                    "Software and Developement": 0.012264685514842619,
                    "Sports": 0.07886599539842308,
                    "Toons": 0.008013224259627298,
                }
            ),
            "label": "Sci/Tech",
        }


def test_predict_es_lang():
    """
    [TO BE IMPLEMENTED]
    Test the "/predict" endpoint, with an input text in Spanish.
    Does the tokenizer and classifier handle this case correctly? Does it return an error?
    """
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "source": "Spanish News",
                "url": "sem-url.com.es",
                "title": "Um textinho de exemplo",
                "description": "Un texto en español sobre deportes extremos",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "scores": pytest.approx(
                {
                    "Business": 0.16356671736718273,
                    "Entertainment": 0.17978778674330217,
                    "Health": 0.08506376704004996,
                    "Music Feeds": 0.010531944211812586,
                    "Sci/Tech": 0.41276170654415456,
                    "Software and Developement": 0.027890526079416365,
                    "Sports": 0.10960605401260183,
                    "Toons": 0.010791498001479693,
                }
            ),
            "label": "Sci/Tech",
        }


def test_predict_non_ascii():
    """
    [TO BE IMPLEMENTED]
    Test the "/predict" endpoint, with an input text that has non-ASCII characters.
    Does the tokenizer and classifier handle this case correctly? Does it return an error?
    """
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "source": "Spanish News",
                "url": "sem-url.com.es",
                "title": "Um textinho de exemplo",
                "description": "U¢¢¢¢ texto en español s§§§§re depor©s extrªªªmos",
            },
        )
        assert response.status_code == 200
        assert response.json() == {
            "scores": pytest.approx(
                {
                    "Business": 0.21092989708811047,
                    "Entertainment": 0.12600053712025616,
                    "Health": 0.07679513076445675,
                    "Music Feeds": 0.009386343365234346,
                    "Sci/Tech": 0.41737619557565453,
                    "Software and Developement": 0.026349905803349713,
                    "Sports": 0.11610028134274683,
                    "Toons": 0.017061708940191118,
                }
            ),
            "label": "Sci/Tech",
        }
