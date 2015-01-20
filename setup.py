#!/usr/bin/env python

import setuptools
import os
import shutil

if not os.path.exists('build/_scripts'):
    os.makedirs('build/_scripts')
shutil.copyfile('pyse_script.py', 'build/_scripts/pyse')

setuptools.setup(
    version='0.0.1',
    name='pyse',
    description='An quite easy python stream editor.',
    author='Cat Cfrco',
    author_email='cfrco@meowdev.tw',
    license='',
    url='https://github.com/cfrco/pyse',
    packages=['pyse', 'pyse.ext'],
    scripts=['build/_scripts/pyse']
)
