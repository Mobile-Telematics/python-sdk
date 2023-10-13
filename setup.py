# setup.py
from setuptools import setup, find_packages

setup(
    name="damoov_admin",
    version="0.6",
    packages=find_packages(),
    install_requires=[
        "requests",
        "sentry_sdk"
    ],
    author="Damoov",
    author_email="admin@damoov.com",
    description="SDK for Damoov's APIs",
    keywords="damoov sdk telematics mobiletelematics safety driving safe-driving fleetmanagement fleet-management fleet driving-behavior driving-behaviour driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring",
)
