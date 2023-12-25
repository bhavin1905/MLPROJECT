from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

requirements=[]
def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Bhavin',
    author_email='bhavinparmar0305@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirenments.txt')
)