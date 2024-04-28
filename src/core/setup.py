from setuptools import setup, find_packages

setup(
    name='outfit_of_the_day',
    version='0.0.1',
    python_requires='>=3.12.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=[
        'aws_lambda_powertools',
        'boto3',
        'botocore',
        'dataclasses-json',
        'requests'
    ]
)
