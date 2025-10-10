
import inspect

def revise(u,v, domains, constraints):

    change = False
    for i in domains[u][:]:
        if not any(all(constraint(i,j) for constraint in constraints) for j in domains[v]):
            domains[u].remove(i)
            change = True
    return domains, change

def init_worklist(gamma):
    worklist = []
    for variables, constraint_func in gamma[2].items():
        worklist.append(variables)
    return worklist 

def ac3(gamma):
    worklist = init_worklist(gamma)
    variables = gamma[0]
    domains = gamma[1]

    while worklist:
        u,v = worklist.pop(0)
        constraints = gamma[2].get((u,v), [])
        
        domains, change = revise(u,v,domains, constraints)
        if change:
            for w in variables:
                if w != v and (w,u) in gamma[2]:
                    worklist.append((w,u))
    return domains
    


V = {'v0','v1'}
D = {
    'v0':[1,2],
    'v1':[1,2,3]
}

C = {
    ('v0','v1'): [
        lambda x,y: x < y,
        
    ]
    
}



gamma = (V,D,C)
final_domains = ac3(gamma)

print(final_domains)


#todo Arc consistency
#todo Backtracking search
#todo Inference
#todo Variable elimination
#todo constraint graph
#
