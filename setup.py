import importlib
import os
import sys
import warnings

from setuptools import find_packages, setup

if sys.version_info[0:2] < (3, 5):
    warnings.warn('This package will only run on Python version 3.5+')

# allow setup.py to be run from any path
cwd = os.getcwd()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

package_info = importlib.import_module('govuk_forms')
with open('README.rst') as readme:
    README = readme.read()

setup_extensions = importlib.import_module('setup_extensions')

setup_requires = ['setuptools', 'pip', 'wheel']
install_requires = ['django>=1.11']
extras_require = {}
tests_require = ['flake8']

setup(
    name='django-govuk-forms',
    version=package_info.__version__,
    author=package_info.__author__,
    url='https://github.com/ministryofjustice/django-govuk-forms',
    packages=find_packages(exclude=['demo', 'tests']),
    py_modules=['setup_extensions'],
    include_package_data=True,
    license='MIT',
    description='Django app that creates forms based on Government Digital Services style guide',
    long_description=README,
    keywords='django,govuk,template,forms,elements,frontend,toolkit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    cmdclass=setup_extensions.command_classes,
    setup_requires=setup_requires,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    test_suite='tests',
)
os.chdir(cwd)