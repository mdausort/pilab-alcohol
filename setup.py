# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 11:19:19 2022

@author: manou
"""

from setuptools import setup
import pilab_alcohol


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='pilab-alcohol',
    version='0.1.2',
    description='Framework of my master thesis on the effect of withdrawal on the white matter of alcoholic patients using dMRI data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mdausort/pilab-alcohol',
    author='Manon Dausort',
    author_email='manon.dausort@uclouvain.be',
    license='BSD 2-clause',
    packages=['pilab_alcohol'],
    install_requires=['numpy',
                      'nibabel',
                      'xlsxwriter',
                      'pandas',
                      'matplotlib',
                      'sklearn',
                      'seaborn',
                      'dipy',
                      'scikit-image',
                      'scipy',
                      'openpyxl'
                      ],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)
