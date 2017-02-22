import os

from setuptools import setup, find_packages

ROOT = os.path.dirname(os.path.realpath(__file__))


setup(
    name='sr',
    version='0.1.0',
    description='Console tool to search and replace'
                ' content in files',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author="Gregory Petukhov",
    author_email='lorien@lorien.name',
    url='http://github.com/lorien/sr',
    packages=find_packages(),
    install_requires=['six'],
    license="MIT",
    keywords="user agent browser navigator",
    entry_points={
        'console_scripts': [
            'sr = sr.base:script_sr',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Utilities',
    ],
)
