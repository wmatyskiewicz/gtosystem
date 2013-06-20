import os
from setuptools import setup, find_packages
from gtosystem import VERSION

release = ".".join(str(num) for num in VERSION)

setup(
    name = "GTO SYSTEM",
    version = release,
    author = "SSQ IT Solutions",
    author_email = "gto@ssq.pl",
    description = ("GTO SYSTEM"),
    url = 'http://www.ssq.pl/',
    keywords = '',
    platforms = ['any'],
    license = 'Apache Software License v2.0',
    packages = find_packages('project'),
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
