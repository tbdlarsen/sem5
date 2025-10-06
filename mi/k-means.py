import sys
def initial_centers(dimension, data):
    init = []
    for i in range(dimension):
        init.append(data[i])
    return init

def initial_clusters(amount_of_clusters):
    clusters = []
    for i in range(amount_of_clusters):
        clusters.append([])
    return clusters

def euclidian_dist(x,y):
    dist = 0
    for i in range(len(x)):
        dist += (x[i]-y[i])**2
    return dist**(1/2)

k = 2

S = [[1,2],[3,4],[1.2,3.4]]
dimension = len(S[1])

clusters = initial_clusters(k)
centers = initial_centers(dimension,S)

dist = sys.float_info.max
closest = 0
for i in range(k):
    new_dist = euclidian_dist(S[0],centers[i])
    if(new_dist < dist):
        dist = new_dist
        closest = i

print(clusters)
clusters[closest].append(S[0])



print(centers)
print(clusters)
