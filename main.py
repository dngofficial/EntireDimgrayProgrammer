import csv 
import math
import random 
# dist = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

clusterCurrentTotalSums = []
clusterCentroidArray = []
clusterCurrentTotalPointsArray = []
clusterCurrentTotalSumsCoordinates = []
clusterPreviousTotalPointsArray = []
inTheLoop = True
iterationsTaken = 0
overallClusterIterationDistanceSum = 0




file = open("coordinates.csv", "r")
l = file.read()
list = l.split("\n")
list.pop()

print("coordinate 10 is " + str(list[10]))

totalClusters = input("How many clusters: ")
print(totalClusters)


values = range(int(totalClusters))
for i in values:
  randomPick = random.randint(0, len(list)-1)
  Arr = list[randomPick].split(",")
  random_coordinates = [float(Arr[0]), float(Arr[1])]
  clusterCentroidArray.append(random_coordinates)
  clusterCurrentTotalPointsArray.append(0)
  clusterPreviousTotalPointsArray.append(0)
  clusterCurrentTotalSums.append(0)
  clusterCurrentTotalSumsCoordinates.append([0,0])




print(clusterCentroidArray)


def assignCoords():
  with open("coordinates.csv", "r") as a_file:
    csvReader = csv.reader(a_file, delimiter=',')
    for row in csvReader:
      clusterCurrentDistancesFromCurrentPoint= []
      current_coordinates = [float(row[0]), float(row[1])]
      for coordinate in clusterCentroidArray:
        minimumDistance = math.dist(coordinate[0:2], current_coordinates)
        clusterCurrentDistancesFromCurrentPoint.append(minimumDistance)        
      minimumDistance = min(clusterCurrentDistancesFromCurrentPoint)
      minimumIdx = clusterCurrentDistancesFromCurrentPoint.index(minimumDistance)
      clusterCurrentTotalPointsArray[minimumIdx] += 1
      
      minimumDistance = minimumDistance ** 2
      clusterCurrentTotalSums[minimumIdx] += minimumDistance
      clusterCurrentTotalSumsCoordinates[minimumIdx][0] += float(row[0])
      clusterCurrentTotalSumsCoordinates[minimumIdx][1] += float(row[1])
      clusterCurrentDistancesFromCurrentPoint = []
      
def calculateCentroids2():
  for index, item in enumerate(clusterCentroidArray):
    x = clusterCurrentTotalSumsCoordinates[index][0]/clusterCurrentTotalPointsArray[index]
    y = clusterCurrentTotalSumsCoordinates[index][1]/clusterCurrentTotalPointsArray[index]
    clusterCentroidArray[index] = [x, y]
  print(clusterCentroidArray)  

assignCoords()
calculateCentroids2()
'''
for index, item in enumerate(clusterCentroidArray):
    totalDis = 0
    totalPoints = 0
    totalSum = 0
    print("Cluster: " + str(clusterCentroidArray[index]))
    print("Sum of distance cluster squared: " + str(clusterCurrentTotalSums[index]))
    totalSum = clusterCurrentTotalSums[index]
    totalDis = totalDis + clusterCurrentTotalSums[index]
    totalPoints = totalPoints + clusterCurrentTotalPointsArray[index]
    print("Total points in cluster: " + str(clusterCurrentTotalPointsArray[index]))
    print("total x = "  + str(clusterCurrentTotalSumsCoordinates[index][0]))
    print("total y = "  + str(clusterCurrentTotalSumsCoordinates[index][1]))
    x = clusterCurrentTotalSumsCoordinates[index][0]/clusterCurrentTotalPointsArray[index]
    y = clusterCurrentTotalSumsCoordinates[index][1]/clusterCurrentTotalPointsArray[index]
    print("new cluster = " + str([x, y]))
    print("-----------------------------------------")
'''

while (inTheLoop):
  
  for index, item in enumerate(clusterCentroidArray):
    totalDis = 0
    totalPoints = 0
    totalSum = 0
    print("Cluster: " + str(clusterCentroidArray[index]))
    print("Sum of distance cluster squared: " + str(clusterCurrentTotalSums[index]))
    totalSum = clusterCurrentTotalSums[index]
    totalDis = totalDis + clusterCurrentTotalSums[index]
    totalPoints = totalPoints + clusterCurrentTotalPointsArray[index]
    print("Total points in cluster: " + str(clusterCurrentTotalPointsArray[index]))
    print("total x = "  + str(clusterCurrentTotalSumsCoordinates[index][0]))
    print("total y = "  + str(clusterCurrentTotalSumsCoordinates[index][1]))
    x = clusterCurrentTotalSumsCoordinates[index][0]/clusterCurrentTotalPointsArray[index]
    y = clusterCurrentTotalSumsCoordinates[index][1]/clusterCurrentTotalPointsArray[index]
    print("new cluster = " + str([x, y]))
    print("-----------------------------------------")
  

  if (clusterCurrentTotalPointsArray == clusterPreviousTotalPointsArray):
    inTheLoop = False
  else:
    print("Current clusters points = " + str(clusterCurrentTotalPointsArray))
    print("Previous clusters points = " + str(clusterPreviousTotalPointsArray))
    clusterPreviousTotalPointsArray = clusterCurrentTotalPointsArray
    
    clusterCurrentTotalPointsArray = []
    clusterCurrentTotalSumsCoordinates = []
    clusterCurrentTotalSums = []
    iterationsTaken += 1

    for i in values:
      clusterCurrentTotalPointsArray.append(0)
      clusterCurrentTotalSums.append(0)
      clusterCurrentTotalSumsCoordinates.append([0,0])
    assignCoords()
    calculateCentroids2()
 
print("Iterations taken: " + str(iterationsTaken))

  
