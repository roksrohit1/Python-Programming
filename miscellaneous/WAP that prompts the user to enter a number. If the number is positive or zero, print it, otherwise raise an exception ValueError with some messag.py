#WAP that prompts the user to enter a number. If
# the number is positive or zero, print it, otherwise
# raise an exception ValueError with some
# message.

try:
    n=int(input("enter the value:"))
    if n>=0:
        print(n,"no error is there")
except ValueError:
        raise ValueError()
print("value error is present")