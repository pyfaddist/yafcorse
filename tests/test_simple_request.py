from flask import Flask, Response
from flask.testing import FlaskClient


def test_simple_request(client: FlaskClient):
    response: Response = client.get('/some-request', headers={
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Origin'.lower() in response.headers
    assert 'Access-Control-Max-Age'.lower() not in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') is not None
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
