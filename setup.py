import os
import sys

from setuptools import setup

this_directory = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(this_directory, 'src/version.py')

try:
    exec(open(version_file).read())
except IOError:
    print("Failed to load PyFlink Docs version file for packaging. " +
          "'%s' not found!" % version_file,
          file=sys.stderr)
    sys.exit(-1)
VERSION = __version__  # noqa

setup(
    name='pyflink-docs',
    version=VERSION,
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'docutils',
        'jinja2',
        'nbconvert!=5.4',
        'traitlets>=5',
        'nbformat',
        'sphinx>=1.8',
    ],
    author='Xingbo',
    author_email='hxbks2ks@gmail.com',
    description='PyFlink Docs',
    long_description=open('README.md').read(),
    license='https://www.apache.org/licenses/LICENSE-2.0',
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Framework :: Jupyter',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
    ],
    zip_safe=True,
)
