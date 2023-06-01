from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="LivingLabScales",
    version="0.1.0",
    description="LivingLabScales python package",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="https://livinglabscales.readthedocs.io/",
    author = "Chidiebere Ibiam",
    author_email="chidiebereorjiibiam7@gmail.com",
    license= "Apache License",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved ::  Apache License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    packages=["LivingLabScales"],
    include_package_data=True,
    install_requires=["requests"]

)