# setup.py
from setuptools import setup, find_packages

setup(
    name="damoov_admin",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "sentry_sdk"
    ],
    author="Damoov",
    author_email="admin@damoov.com",
    description="SDK for Damoov's APIs",
    keywords="damoov sdk",
)
