import setuptools
import os


def getversion():
    """
    read the version string from __init_.py
    """
    # get the init file path
    thispath = os.path.abspath(os.path.dirname(__file__))+"/"
    initfile = thispath + "smindex/__init__.py"

    # read the file in
    f = open(initfile, "r")
    lines = f.readlines()
    f.close()

    # search for the version
    version = "unknown"
    for item in lines:
        if "__version__" in item:
            s = item.split("=")
            version = s[-1].strip().strip('"').strip("'")
            break
    return version


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="smindex",
    version=getversion(),
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
        "numpy",
        "DateTimeTools",
        "requests",
        "tqdm",
    ],
)
