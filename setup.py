import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="data_generator-pmattd",  # Replace with your own username
    version="0.0.1",
    author="Peter Duncan",
    author_email="author@example.com",
    description="tool for generating fake data for either streaming or batch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pmattd/big-data-generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
