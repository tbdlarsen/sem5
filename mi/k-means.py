import sys
def initial_centers(k, data):
    init = []
    for i in range(k):
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

def init_new_centers(dimension, amount_of_clusters):
    new_centers = []
    for i in range(amount_of_clusters):
        new_centers.append([])
        for j in range(dimension):
            new_centers[i].append(0)
    
    return new_centers


def new_centers(clusters, dimension):
    centers = init_new_centers(dimension, len(clusters))
    for i in range(len(centers)):
        centers[i] = get_new_center(clusters[i],dimension)
    return centers

def center_difference(old_centers, new_centers):
    tolerance = 1e-6
    for old,new in zip(old_centers,new_centers):
        if (euclidian_dist(old,new) > tolerance):
            return True
    return False

k = 2

S = [[1,2],[3,4],[1.2,3.4]]
dimension = len(S[0])

clusters = initial_clusters(k)
centers = initial_centers(k,S)
clusters = assign_datapoints(S,centers,k,clusters)
next_centers= new_centers(clusters,dimension)


print(clusters)
print(centers)
print()

while(center_difference(centers,next_centers)):
    clusters = initial_clusters(k)
    centers = next_centers
    clusters = assign_datapoints(S,centers,k,clusters)
    next_centers= new_centers(clusters,dimension)

    print(clusters)
    print(centers)
    print()



print("final")
print(clusters)
print(centers)
print()
        




