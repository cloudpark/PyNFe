#!/usr/bin/env python
import setuptools

setuptools.setup(
    name='PyNFe',
    version='1.0.1',
    author='TadaSoftware',
    author_email='tadasoftware@gmail.com',
    url='https://github.com/TadaSoftware',
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    package_data={
        'pynfe': ['data/**/*.txt'],
    },
    install_requires=[
        'pyopenssl',
        'requests',
        'lxml',
        'signxml',
    ],
    extras_require={
        'nfse': [
            'suds-jurko',
            'pyxb==1.2.4',
        ],
    },
    zip_safe=False,
    python_requires='>=3.6',
)
