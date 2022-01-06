import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_pypi_project",
    version = "0.0.4",
    author = "Eugene Schava",
    author_email = "echava@gmail.com",
    description = ("a cross-platform utility for reporting system and processes utilization (CPU, memory, disks, network) using MQTT protocol"),
    license = "MIT",
    keywords = "",
    url = "https://github.com/eschava/psmqtt",
    packages=['psmqtt'],
    long_description=read('README')
)
