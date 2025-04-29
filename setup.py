from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This is used to read the requirements file.Its takes the file path
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLEndtoEndProject',
    version='0.1.0',
    author='NaveenaChatti',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 