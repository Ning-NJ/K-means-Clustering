import random
import math

# make code more efficient and add an algorithm that chooses k

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def isEqual(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

def dist(p1, p2):
    return math.sqrt(math.pow(p1.getX() - p2.getX(), 2) + math.pow(p1.getY() - p2.getY(), 2))

def randomCoords(amount, minX, maxX, minY, maxY, clusterNum, spread):
    # to improve the purpose of this program, we're gonna make it less random and more grouped to see it better
    coords = []
    centers = []

    for i in range(clusterNum):
        centers.append((random.randint(minX + spread * 2, maxX - spread * 2), random.randint(minY + spread * 2, maxY - spread * 2)))

    for centerX, centerY in centers:
        for i in range((int)(amount/clusterNum)):
            while True:
                x = random.gauss(centerX, spread)
                y = random.gauss(centerY, spread)

                if minX <= x <= maxX and minY <= y <= maxY:
                    coords.append(Point(x, y))
                    break
    return coords

def placeCentroid(cenAmount, minX, maxX, minY, maxY):
    centroids = []
    for i in range(int(cenAmount)):
        centroids.append(Point(random.randint(minX, maxX), random.randint(minY, maxY)))
    return centroids

def assignToCluster(coords, centroids):
    clusters = [[] for _ in range(len(centroids))] # creates a cluster for each centroid

    for i in range(len(coords)):
        point = coords[i]
        # compute distance from each centroid then assign into clusters A, B, ... K
        # store points as index of coords in cluster A as coords[0], coords[1]...
        bestCluster = 0
        bestDist = dist(point, centroids[0])

        for j in range(1, len(centroids)):
            distance = dist(point, centroids[j])
            if distance < bestDist:
                bestDist = distance
                bestCluster = j

        clusters[bestCluster].append(i)

    return clusters

def findNewCentroid(clusters, coords):
    centroids = []
    for cluster in clusters:
        if len(cluster) == 0:
            centroids.append(random.choice(coords))
            continue
        xSum = 0
        ySum = 0
        for index in cluster:
            xSum += coords[index].getX()
            ySum += coords[index].getY()

        centroids.append(Point(xSum/len(cluster), ySum/len(cluster)))
        
    return centroids

def kMean(coords, minX, maxX, minY, maxY, cenAmount, tol = 0.0001, maxIter = 100):
    #coords are coordinates, cenAmount is k, tol is centroid shift tolerance, maxIter is maximum iterations
    centroids = placeCentroid(cenAmount, minX, maxX, minY, maxY)
    
    for i in range(maxIter):
        clusters = assignToCluster(coords, centroids)
        newCen = findNewCentroid(clusters, coords)
        shift = 0
        for i in range((int)(cenAmount)):
            shift += dist(centroids[i], newCen[i])

        centroids = newCen
        if shift < tol:
            break
    
    return clusters, centroids

def silhouetteScoring(clusters, centroids, coords):
    #step 1: make a loop fo each point in each cluster
    #step 2: find the distance from other points in the cluster 
    #use dictionary to make finding distance more efficient
    #when you create key from a to b you also create one for b to a, assign same value. search for key first then create
    for cluster in range (len(clusters)):
        for
