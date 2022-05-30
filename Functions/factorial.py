def fact(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
a=int(input('enter no. '))
out=fact(a)
print(out)