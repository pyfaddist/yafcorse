from flask import Response
from flask.testing import FlaskClient


# def test_with_origin(client: FlaskClient):
#     response: Response = client.options('/some-request', headers={
#             'Access-Control-Request-Method': 'POST',
#             'Access-Control-Request-Headers': 'Content-Type, X-Custom',
#             'Origin': 'https://test.org'
#         })
#     assert response.status_code == 404
#     assert 'Access-Control-Max-Age' in response.headers
#     assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'


def test_with_origin(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Origin'.lower() in response.headers
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') is not None
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
    assert response.headers.get('Access-Control-Max-Age') is not None
    assert response.headers.get('Access-Control-Max-Age') != ''


def test_without_origin(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Origin'.lower() not in response.headers
    assert 'Access-Control-Max-Age'.lower() not in response.headers
    assert 'Access-Control-Allow-Methods'.lower() not in response.headers
    assert 'Access-Control-Allow-Headers'.lower() not in response.headers


def test_allow_method(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
            'Access-Control-Request-Method': 'POST',
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Methods'.lower() in response.headers
    assert 'POST' in response.headers.get('Access-Control-Allow-Methods')
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
    assert 'Access-Control-Allow-Headers'.lower() not in response.headers


def test_dont_allow_method(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
            'Access-Control-Request-Method': 'PATCH',
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Methods'.lower() not in response.headers
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
    assert 'Access-Control-Allow-Headers'.lower() not in response.headers


def test_allow_headers(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
            'Access-Control-Request-Headers': 'Content-Type, X-Test-Header',
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Headers'.lower() in response.headers
    assert 'Content-Type' in response.headers.get('Access-Control-Allow-Headers')
    assert 'X-Test-Header' in response.headers.get('Access-Control-Allow-Headers')
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
    assert 'Access-Control-Allow-Methods'.lower() not in response.headers


def test_dont_allow_headers(client: FlaskClient):
    response: Response = client.options('/some-request', headers={
            'Access-Control-Request-Headers': 'Content-Type, X-Test-Header, X-Not-Allowed',
            'Origin': 'https://test.org'
        })
    assert response.status_code == 404
    assert 'Access-Control-Allow-Headers'.lower() not in response.headers
    assert 'Access-Control-Max-Age'.lower() in response.headers
    assert response.headers.get('Access-Control-Allow-Origin') == 'https://test.org'
    assert 'Access-Control-Allow-Methods'.lower() not in response.headers
