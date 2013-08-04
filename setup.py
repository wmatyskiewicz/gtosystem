import os, sys

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.rst') as f:
    readme = f.read().splitlines()

current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, current_dir + os.sep + 'src')

setup(
    name = "gtosystem",
    version = __import__('gtosystem').get_version(),
    author = "SSQ IT Solutions",
    author_email = "gto@ssq.pl",
    url = 'http://www.ssq.pl/',
    description = readme,
    keywords = 'GTO System',
    platforms = ['any'],
    license = 'Apache Software License v2.0',
    packages = find_packages('src'),
    include_package_data = True,
    package_dir = {'':'src'},
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
    install_requires=required,
    entry_points={
        'console_scripts': [
            'gtosystem = gtosystem.__main__:main',
        ],
    },
)
