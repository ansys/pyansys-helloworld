"""Sphinx Bootstrap Theme package."""
import codecs
import os
from io import open as io_open

from setuptools import setup

# Use single source package versioning
# loosely from https://packaging.python.org/guides/single-sourcing-package-version/
HERE = os.path.abspath(os.path.dirname(__file__))
__version__ = None
version_file = os.path.join(HERE, 'ansys', 'examples', 'greeter_client', '_version.py')
with io_open(version_file, mode='r') as fd:
    exec(fd.read())


def read(rel_path):
    with codecs.open(os.path.join(HERE, rel_path), 'r') as fp:
        return fp.read()


# Get the long description from the README file
with open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['grpcio>=1.30.0',
                    'ansys-api-greeter-example-v1==0.1.0']

setup(
    name='ansys-examples-greeter-client',
    packages=['ansys.examples.greeter_client'],
    version=__version__,
    description='Example greeter client',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/pyansys/pyansys-package-example/',
    license='MIT',
    author='ANSYS, Inc.',
    maintainer='Alexander Kaszynski',
    maintainer_email='alexander.kaszynski@ansys.com',
    install_requires=install_requires,
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
