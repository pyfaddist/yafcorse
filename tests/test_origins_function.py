import pytest
from flask import Flask, Response
from flask.testing import FlaskClient

from yafcorse import Yafcorse


@pytest.fixture()
def local_app():
    app = Flask(__name__)

    cors = Yafcorse({
        'allowed_methods': ['GET', 'POST', 'PUT'],
        'allowed_headers': ['Content-Type', 'X-Test-Header'],
        'origins': lambda origin: origin == 'https://from_lambda'
    })
    cors.init_app(app)

    return app


@pytest.fixture()
def local_client(local_app: Flask):
    return local_app.test_client()


def test_origin_function(local_client: FlaskClient):
    response: Response = local_client.options('/some-request', headers={
            'Origin': 'https://from_lambda'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Origin'.lower() in response.headers
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') is not None
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://from_lambda'
    assert response.headers.get('Access-Control-Max-Age') is not None
    assert response.headers.get('Access-Control-Max-Age') != ''


def test_origin_function_fail(local_client: FlaskClient):
    response: Response = local_client.options('/some-request', headers={
            'Origin': 'https://other_than_lambda'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Origin'.lower() not in response.headers
    assert 'Access-Control-Max-Age'.lower() not in response.headers
