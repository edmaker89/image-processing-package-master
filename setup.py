from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="image_processing_ed",
    version="0.0.1",
    author='__token__',
    author_email="edmaker@gmail.com",
    description="Image Processor",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edmaker89/image-processing-package-master",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.12"
)