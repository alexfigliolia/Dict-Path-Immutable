import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dict_Path_Immutable",
    version="0.2",
    author="Alex Figliolia",
    author_email="alexfigliolia@gmail.com",
    description="Modify deep dictionary properties without modifying the original dictionary (immutability)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexfigliolia/Object-Path-Immutable-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

