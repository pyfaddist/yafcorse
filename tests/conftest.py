import pytest
from flask import Flask

from yafcorse import Yafcorse


@pytest.fixture()
def app():
    app = Flask(__name__)

    cors = Yafcorse({
        'origins': '*',
        'allowed_methods': ['GET', 'POST', 'PUT'],
        'allowed_headers': ['Content-Type', 'X-Test-Header'],
        'allow_credentials': True,
        'cache_max_age': str(60 * 5)
    })
    cors.init_app(app)

    return app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()
