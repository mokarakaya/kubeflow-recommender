
import setuptools

with open("kubeflow-recommender/README.md", "r") as fh:
    long_description = fh.read()


with open('kubeflow-recommender/requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="kubeflow-recommender",
    version="0.0.1",
    author="mokarakaya",
    author_email="mokarakaya@gmail.com",
    description="Recommender engine built with kubeflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mokarakaya/kubeflow-recommender",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)