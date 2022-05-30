a={'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20}
b=[]
c=dict()
for i,j in a.items():
    if j not in b:
        b.append(j)
        c[i]=j
print(c)