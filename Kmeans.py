import random
import math

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

def randomCoords(amount, minX, maxX, minY, maxY):
    coords = []
    for i in range(int(amount)):
        coords.append(Point(random.randint(minX, maxX), random.randint(minY, maxY)))
    return coords

def placeCentroid(cenAmount, minX, maxX, minY, maxY):
    cenCoords = []
    for i in range(int(cenAmount)):
        cenCoords.append(Point(random.randint(minX, maxX), random.randint(minY, maxY)))
    return cenCoords

def centroidDistance(coords, cenCoords):
    cenDistance = []
    for coord in coords:
        dataForCoord = []
        dataForCoord.append(coord)
        for i in range(len(cenCoords)):
            dataForCoord.append(math.sqrt(math.pow(coord.getX() - cenCoords[i].getX(), 2)+math.pow(coord.getY() - cenCoords[i].getY(), 2)))
        cenDistance.append(dataForCoord)
    return cenDistance

def assignToCentroid(cenDistance, cenAmount):
    closestCentroid = []
    for amount in range (int(cenAmount)):
        blankList = []
        closestCentroid.append(blankList)
    for i in range(len(cenDistance)):
        smallest = cenDistance[i][1]
        index = 0
        for j in range(2, len(cenDistance[i])):
            if cenDistance[i][j] < smallest:
                smallest = cenDistance[i][j]
                index = j-1
        closestCentroid[index].append(cenDistance[i][0])
    return closestCentroid

def meanFinder(closestCentroid, cenAmount, coords):
    meanedCen = []
    for i in range (int(cenAmount)):
        if len(closestCentroid[i]) == 0:
            meanedCen.append(random.choice(coords))
            continue
        xsum = 0.0
        ysum = 0.0
        for point in closestCentroid[i]:
            xsum += point.getX()
            ysum += point.getY()
        point = Point(xsum/(len(closestCentroid[i])), ysum/(len(closestCentroid[i])))
        meanedCen.append(point)
    return meanedCen

def kMean(coords, minX, maxX, minY, maxY, cenAmount):
    cenCoords = placeCentroid(cenAmount, minX, maxX, minY, maxY)
    cenDistance = centroidDistance(coords, cenCoords)
    closestCen = assignToCentroid(cenDistance, cenAmount)
    newCentroids = meanFinder(closestCen, cenAmount, coords)
    while True:
        for i in range(int(cenAmount)):
            if newCentroids[i].isEqual(cenCoords[i]):
                if i == cenAmount - 1:
                    resultWithCen = [closestCen, newCentroids]
                    return resultWithCen
                continue
            else:
                break
        cenCoords = newCentroids
        cenDistance = centroidDistance(coords, cenCoords)
        closestCen = assignToCentroid(cenDistance, cenAmount)
        newCentroids = meanFinder(closestCen, cenAmount, coords)