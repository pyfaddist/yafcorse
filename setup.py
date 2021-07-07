from distutils.core import setup

import setuptools

setup(
    name='flask_cors',
    version='1.0',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    url='',
    license='EULA',
    author='Christian Dein',
    author_email='christian.dein@dein-hosting.de',
    description='Enable CORS for flask applications'
)
