from typing import List
from setuptools import setup, find_packages

def get_requirements(file_path:str) -> List[str]:
    """
    This function reads the requirements file and returns a list of packages.
    """
    requirements = []
    
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='ML-Project',
    version='0.1.0',
    author='Mohammed Saqib',
    author_email="saqibmohammed215@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
