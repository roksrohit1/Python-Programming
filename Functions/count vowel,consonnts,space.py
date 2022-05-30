def alph(a):
    vow=0
    space=0
    const=0
    for i in range(len(a)):
        if a[i] in (['a','e','i','o','u'] or ['A','E','I','O','U']):
            vow+=1
        elif a[i]==' ':
            space+=1
        else:
            const+=1
    print('vowel=',vow ,'consonant = ',const,'space = ',space)
x=input('enter any word ')
alph(x)