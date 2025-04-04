from setuptools import setup, find_packages


with open('/Users/rolf/Downloads/README.md', 'r') as f:
    global description
    description = f.read()

setup(
    name="requestt_pro",  
    version="0.0.5",
    python_requires='>=3.11.1',
    url="https://github.com/wedwedwed495/wedwedwed495",
    description="A brief description of your package",
    long_description=description,  
    long_description_content_type='text/markdown',
    packages=find_packages(),
)
