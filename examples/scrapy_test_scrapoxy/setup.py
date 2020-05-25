# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name         = 'scrapy_scrapoxy_example',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = cloud_test.settings']},
)
