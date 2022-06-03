from setuptools import setup, find_packages

setup(
    author="Daniel Cho",
    description="A complete package for linear regression.",
    name="so2-emission",
    version="0.1.0",
    packages=find_packages(include=["so2_emission", "so2_emission.*"]),
    install_requires=[
        'pandas>=1.3',
        'numpy==1.21',
        'matplotlib>=3.5.1,<4'],
)
