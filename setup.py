from setuptools import find_packages, setup

def get_packages(requirements_path):
    packages = []
    with open(requirements_path) as obj:
        lines = obj.readlines()
        packages = [package for package in lines if packages != '- e .']
    return packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='muhammadshah',
    author_email='muhammadof9@gmail.com',
    install_requires=get_packages('requirements.txt'),
    packages=find_packages(),
)