import os
import re
from setuptools import setup


def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description(long_description_file):
    with open(long_description_file, encoding='utf-8') as f:
        long_description = f.read()

    return long_description


version = get_version('slydes')


setup(
    name='slydes',
    version=version,
    url='https://github.com/jonatasbaldin/slydes',
    license='MIT',
    description='Why not show your presentations with Python?',
    long_description=get_long_description('README.md'),
    long_description_content_type='text/markdown',
    packages=['slydes'],
    author='Jonatas Baldin',
    author_email='jonatas.baldin@gmail.com',
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics :: Presentation',
    ],
)
