import argparse

# Read the args and put them in variables
parser = argparse.ArgumentParser()
parser.add_argument("K", type=int)
parser.add_argument("N", type=int)
parser.add_argument("d", type=int)
parser.add_argument("MAX_ITER", type=int)
args = parser.parse_args()
K = args.K
N = args.N
d = args.d
MAX_ITER = args.MAX_ITER

# Assertions
assert K > 0 and N > 0 and d > 0 and MAX_ITER > 0
assert K < N


# Get list of index of observations and calc their avg
def calc_centroid(lst):
    centroid = [0] * d
    count = len(lst)
    for i in range(count):
        for j in range(d):
            centroid[j] += observations[lst[i]][j]
    centroid = [x / count for x in centroid]
    return centroid


# Get 2 observations and calc their distance
def euclidian_distance(a, b):
    dist = 0
    for i in range(d):
        dist += (a[i] - b[i]) ** 2
    return dist


# Get observation index and centroids and return the closest centroid
def find_closest_centroid(ind, centroids):
    min_dist = -1
    min_cent = 0
    for k in range(K):
        distance = euclidian_distance(observations[ind], centroids[k])
        if distance < min_dist or min_dist == -1:
            min_dist = distance
            min_cent = k
    return min_cent


# Check if new_centroids equal centroids
def check_if_equals(new_centroids, centroids):
    for i in range(K):
        for j in range(d):
            if new_centroids[i][j] != centroids[i][j]:
                return False
    return True


# Calc centroids while num of iter <= MAX_ITER and last(centroids) != centroids
def approximation_loop(centroids):
    for j in range(MAX_ITER):
        clusters = [[] for i in range(K)]
        for i in range(N):
            ind = find_closest_centroid(i, centroids)
            clusters[ind].append(i)
        new_centroids = [None] * K
        for i in range(K):
            new_centroids[i] = calc_centroid(clusters[i])
        if check_if_equals(new_centroids, centroids):
            break
        centroids = new_centroids
    return centroids


# Read from input
observations = [[] for i in range(N)]
centroids = []
i = 0
while True:
    try:
        for num in input().split(','):
            observations[int(i / d)].append(float(num))
            i += 1
    except EOFError:
        break
for i in range(K):
    centroids.append(observations[i])

# Calc centroids
centroids = approximation_loop(centroids)

# Print centroids
for i in range(len(centroids)):
    temp = ["{:.2f}".format(float(c)) for c in centroids[i]]
    print(*temp, sep=",")
