from my_module import functions
from my_module import more_functions
import my_module


"""
A program to demonstrate using Python code from a 
module that comprises more than one file.
"""
functions.fun1()  # From my_module/functions.py
more_functions.fun2()  # From my_module/more_functions.py
my_module.fun3()  # From my_module/__init__.py
