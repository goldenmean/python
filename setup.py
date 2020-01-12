#import setuptools
#from setuptools import setup, find_packages, Extension, Command
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


setup(
    ext_modules = cythonize("cyt_hello_world.pyx")
)