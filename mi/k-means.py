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

def euclidian_dist(x,y) -> float:
    dist = 0
    for i in range(len(x)):
        dist += (x[i]-y[i])**2
    return dist**(1/2)

def get_closest_cluster(amount_of_clusters, centers, data_point):
    distance = sys.float_info.max
    closest = 0
    for i in range(amount_of_clusters):
        new_distance = euclidian_dist(data_point,centers[i])
        if(new_distance < distance):
            distance = new_distance
            closest = i
    return closest

def assign_datapoints(data_points, centers, amount_of_clusters, clusters):
    for data_point in data_points:
        closest_cluster = get_closest_cluster(amount_of_clusters, centers, data_point)
        clusters[closest_cluster].append(data_point)
    return clusters

def get_new_center(cluster,dimension):
    new_center = []
    for dim in range(dimension):
        new_center.append(0)
        for point in cluster:
            new_center[dim] += point[dim]
        new_center[dim] /= len(cluster)

    return new_center

k = 2

S = [[1,2],[3,4],[1.2,3.4]]
dimension = len(S[0])

clusters = initial_clusters(k)
centers = initial_centers(dimension,S)
clusters = assign_datapoints(S,centers,k,clusters)

new_centers = []
for i in range(k):
    new_centers.append([])
    for j in range(dimension):
        new_centers[i].append(0)
        
print(new_centers)
print(clusters)
print(centers)
print()

new_centers[0] = get_new_center(clusters[0],dimension)


print(new_centers)





