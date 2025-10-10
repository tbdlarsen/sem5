
import inspect

def revise(gamma, point):

    change = False
    domains = gamma[1]
    constraints = gamma[2].get((point), [])

    u,v = point
    for i in D[u][:]:
        if not any(all(constraint(i,j) for constraint in constraints) for j in domains[v]):
            domains[u].remove(i)
            change = True
    return gamma, change

def init_worklist(gamma):
    worklist = []
    for variables, constraint_func in gamma[2].items():
        worklist.append(variables)
    return worklist 

def ac3(gamma):
    worklist = init_worklist(gamma)
   

    gamma, change = revise(gamma,worklist[0])
    print("change: ", change)
    return gamma
    


V = {'v0','v1'}
D = {
    'v0':[1,2,3,4],
    'v1':[1,2,3],
    'v2':[0,2,3]
}

C = {
    ('v0','v1'): [
        lambda v0,v1: v0 != v1,
        lambda v0,v1: v0 < v1
    ],
    ('v1','v2'): [
        lambda v1,v2: v1 < v2
    ]
    
}



gamma = (V,D,C)
worklist = ac3(gamma)

print(gamma)

print(worklist)


#todo Arc consistency
#todo Backtracking search
#todo Inference
#todo Variable elimination
#todo constraint graph
#
