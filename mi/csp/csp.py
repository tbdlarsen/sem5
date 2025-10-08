
V = {'A','B'}
D = {
    'A':[1,2],
    'B':[1,2]
}

C = {
    ('A','B'): lambda a,b: a!=b,
    ('A','B'): lambda a,b: a<b
}

gamma = (V,D,C)
#print(gamma)