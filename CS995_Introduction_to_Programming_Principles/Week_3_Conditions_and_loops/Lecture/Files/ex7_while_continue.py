"""
A program to demonstrate continue with a while loop.
This program will continue forever, until ctrl-c is
pressed to stop it.
"""

i = 0
while i < 3:
    print(i)
    if i == 2:
        continue
    i += 1
