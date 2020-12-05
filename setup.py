from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flaskapp",
    version="0.0",
    description="App for IA Pau Data Challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "flask",
        "python-dotenv",
        # "pytorch",
        # "torchvision",
    ],
    packages=find_packages(),
)