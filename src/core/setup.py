from setuptools import setup, find_packages

setup(
    name='core',
    version='0.0.1',
    python_requires='>=3.10.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=[
        'aws_lambda_powertools',
        'boto3',
        'botocore',
        'dataclasses-json',
        'requests'
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Other Environment',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10'
    ]
)
