from setuptools import find_packages, setup
from typing import List

HyphenE = "-e."
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HyphenE in requirements:
            requirements.remove(HyphenE)
    return requirements

setup(
    name='Live-ML-Segmentation',
    version='0.0.1',
    author='yamalies',
    author_email='yamalchrischan@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
