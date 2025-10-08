
import inspect

def revise(gamma, u, v, D, constraint):
    for i in D[u]:
       if not any(constraint(i,j) for j in D[v]):
        D[u].remove(i)


    return gamma


V = {'v0','v1'}
D = {
    'v0':[1,2],
    'v1':[1]
}

C = {
    ('v0','v1'): lambda v0,v1: v0!=v1
}
gamma = (V,D,C)
gamma = revise(gamma, 'v0','v1', D, C[('v0','v1')])
print(gamma)
