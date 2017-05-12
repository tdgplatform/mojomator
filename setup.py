"""
    Mojomator

    Music Compostion Automation and Machine Learning

"""
from setuptools import setup, find_packages

setup(
    name='mojomator',
    version='0.0.1',
    install_requires=[
        'Click',
        'simplejson'
    ],
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        mojomator=cli.mojomator:cli
    '''
)

