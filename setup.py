import pathlib

from setuptools import find_packages
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    description="RabbitMQ-subprocess-client is a RabbitMq client (based on `pika`) spawning tasks as subprocess, allowing handling segfault gracefully. ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/bimdata/rabbitmq-subprocess-client",
    author="Hugo Duroux",
    author_email="hugo@bimdata.io",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=(".github",)),
    include_package_data=True,
    install_requires=["pika"],
)
