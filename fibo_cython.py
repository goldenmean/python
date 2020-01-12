#!/bin/python
#import setuptools
import pyximport; pyximport.install()
import fibo

a = fibo.fib(36)
print(a)