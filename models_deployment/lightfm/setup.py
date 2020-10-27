from setuptools import setup
from setuptools import find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="lightfm_model",
    version="0.1",
    scripts=["lightfm_predictor.py"],
    install_requires=required,
    packages=find_packages(),
    include_package_data=True

)
