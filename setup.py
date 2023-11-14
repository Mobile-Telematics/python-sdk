# setup.py
from setuptools import setup, find_packages

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="damoov_admin",
    version="0.7.6",
    packages=find_packages(),
    install_requires=[
        "requests",
        "sentry_sdk"
    ],
    author="Damoov",
    author_email="admin@damoov.com",
    description="SDK for Damoov's APIs",
    long_description=long_description,  # This line includes the README contents as the description
    long_description_content_type="text/markdown",  # Specifies the format of the long description
    keywords="damoov sdk telematics mobiletelematics safety driving safe-driving fleetmanagement fleet-management fleet driving-behavior driving-behaviour driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring driving-behavior-analysis driving-behaviour-analysis driving-behavior-monitoring driving-behaviour-monitoring driving-behavior-score driving-behaviour-score driving-behavior-scoring driving-behaviour-scoring",
)
