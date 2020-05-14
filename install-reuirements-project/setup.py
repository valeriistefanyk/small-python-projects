from setuptools import setup, find_packages
from os.path import join, dirname

import helloworld

setup(
    name = 'helloworld',
    author='Valerii Stefanyk',
    author_email='valeriistefanyk@gmail.com',
    description='Simple hello world app',
    version=helloworld.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    
    entry_points={
        'console_scripts':
            [
                'helloworld = helloworld.core:print_message',
                'serve = helloworld.web:run_server',
            ]
    },
    include_package_data=True,
    install_requires=['Flask'],
    test_suite='tests',
)