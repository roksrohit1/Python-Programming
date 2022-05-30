#. Write a Python program to read a random line from a file
import random
file=open("apple.txt")
a=file.read().splitlines()
print(a)
b=random.choices(a)
print(b)