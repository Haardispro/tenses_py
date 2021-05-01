import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tense_py",
    version="0.0.0",
    author="Haard Majmudar",
    author_email="haardmajmudar2827@email.com",
    description="This module converts tenses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Haardispro/tenses_py",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
