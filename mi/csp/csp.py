
import inspect

def revise(gamma, u, v, constraints):
    D = gamma[1]
    for i in D[u][:]:
        if not any(all(constraint(i,j) for constraint in constraints) for j in D[v]):
            D[u].remove(i)
    return gamma





V = {'v0','v1'}
D = {
    'v0':[1,2,3,4],
    'v1':[1,2,3]
}

C = {
    ('v0','v1'): [
        lambda v0,v1: v0 != v1,
        lambda v0,v1: v0 < v1
    ]
    
}
gamma = (V,D,C)

for variables, constraint_func in gamma[2].items():
    var1, var2 = variables
    gamma = revise(gamma, var1, var2,constraint_func)


print(gamma)


#todo Arc consistency
#todo Backtracking search
#todo Inference
#todo Variable elimination
#todo constraint graph
#
