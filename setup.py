import os
from setuptools import setup

project_name = "autocoder"
version = "0.0.1"

# Read the long description from README.md and filter out lines with <img
with open("README.md", "r") as fh:
    long_description = fh.read()
    long_description = "\n".join([line for line in long_description.split("\n") if "<img" not in line])

# Read requirements from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().strip().splitlines()

setup(
    name=project_name,
    version=version,
    description="Code that basically writes itself",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AutonomousResearchGroup/autocoder",
    author="Moon",
    author_email="shawmakesmagic@gmail.com",
    license="MIT",
    packages=[project_name],
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
