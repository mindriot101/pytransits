#!/usr/bin/env python

from setuptools import setup
from setuptools.extension import Extension
from Cython.Distutils import build_ext
from numpy import get_include

package_name = 'transitgen'

ext_modules = [
    Extension(
        "{}._Modelgen".format(package_name),
        ['{}/_Modelgen.pyx'.format(package_name),
            'Modelgen/src/GenerateModel.cpp'],
        language="c++", include_dirs=['Modelgen/include', get_include()]),
]

setup(name=package_name,
      version='0.0.1',
      author='Simon Walker',
      author_email='s.r.walker101@googlemail.com',
      license='MIT',
      packages=[package_name, ],
      ext_modules=ext_modules,
      cmdclass={'build_ext': build_ext, }
      )
