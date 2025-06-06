from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if '-e .' in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author='Nagamohan',
    author_email='nagak789@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)