import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name='Object_Path_Immutable',  
  version='0.1',
  scripts=['Object_Path_Immutable'] ,
  author="Alex Figliolia",
  author_email="alexfigliolia@gmail.com",
  description="Modify deep object properties without modifying the original object (immutability)",
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