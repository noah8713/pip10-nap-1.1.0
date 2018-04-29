import uuid

__author__ = 'David Barroso <dbarrosop@dravetech.com>'
from setuptools import setup, find_packages
#from pip.req import parse_requirements

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


#install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
#reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm",
    version="1.1.0",
    packages=find_packages(),
    author="David Barroso",
    author_email="dbarrosop@dravetech.com",
    description="Network Automation and Programmability Abstraction Layer with Multivendor support",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/napalm-automation/napalm",
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt')
)
