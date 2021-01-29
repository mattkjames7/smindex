import setuptools
from setuptools.command.install import install
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smindex",
    version="1.0.0",
    author="Matthew Knight James",
    author_email="mattkjames7@gmail.com",
    description="A tiny module for reading SuperMAG indices and substorm lists.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mattkjames7/smindex",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
    ],
    install_requires=[
		'numpy',
		'RecarrayTools',
		'PyFileIO',
		'DateTimeTools',
	],
)



