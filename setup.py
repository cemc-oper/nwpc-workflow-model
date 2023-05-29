# coding: utf-8
from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nwpc-workflow-model',

    version='0.5.0',

    description='A workflow model using in operation systems at CEMC/CMA.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/cemc-oper/nwpc-workflow-model',

    author='perillaroc',
    author_email='perillaroc@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],

    keywords='cemc workflow model',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=[],

    extras_require={
        'test': ['pytest'],
        'cov': ['pytest-cov', 'codecov']
    },

    entry_points={}
)
