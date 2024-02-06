import sys
import os
import codecs
from setuptools import setup, find_packages


version = '0.4.dev1'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requires = [
    'Django>=1.11',
]


test_requires = [
]


setup(
    name='django-simple-csp',
    version=version,
    description='Django Content Security Policy support.',
    long_description=read('README.rst'),
    author='Nils Rokita, Henning Pridöhl',
    author_email='github@rokita.it',
    maintainer='Nils Rokita',
    maintainer_email='github@rokita.it',
    url='https://github.com/fsinfuhh/django-simple-csp',
    license='License :: OSI Approved :: MIT License',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
        'Framework :: Django',
    ]
)
