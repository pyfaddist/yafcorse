from flask.app import Flask

from yafcorse import Yafcorse


def test_extension(app: Flask):
    assert app.extensions.get('yafcorse') is not None
    assert isinstance(app.extensions.get('yafcorse'), Yafcorse)
