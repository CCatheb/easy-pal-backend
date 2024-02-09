from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Easy PAL Backend",
    version="0.0.1",
    author="Cédric Cathebras",
    author_email="cathebras-cedric@orange.fr",
    description="Ce projet est une API pour le backend du site PAL.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="not_released",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=[
        "flask",
        "psycopg2-binary"
    ],
)
