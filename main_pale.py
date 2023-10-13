import csv 
import math
import random 

clusterCurrentTotalSums = []
clusterCentroidArray = []
clusterCurrentTotalPointsArray = []
clusterCurrentTotalSumsCoordinates = []
clusterPreviousTotalPointsArray = []
inTheLoop = True


totalClusters = input("How many clusters: ")
print(totalClusters)

file = open("coordinates.csv", "r")
l = file.read()
list = l.split("\n")
list.pop()

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
        #print("distance of " + str(minimumDistance) + " goes with" + str(coordinate))
  
        
        #print(clusterCurrentDistancesFromCurrentPoint)
        
      minimumDistance = min(clusterCurrentDistancesFromCurrentPoint)
      minimumIdx = clusterCurrentDistancesFromCurrentPoint.index(minimumDistance)
      clusterCurrentTotalPointsArray[minimumIdx] += 1
  
      
      #print("Current coordinate of " + str(current_coordinates) + "belongs to cluster " + str(clusterCentroidArray[minimumIdx]) + "with a distance of " + str(minimumDistance))
      
      
  
      minimumDistance = minimumDistance ** 2
      clusterCurrentTotalSums[minimumIdx] += minimumDistance
      clusterCurrentTotalSumsCoordinates[minimumIdx][0] += float(row[0])
      clusterCurrentTotalSumsCoordinates[minimumIdx][1] += float(row[1])
      
  
  
      clusterCurrentDistancesFromCurrentPoint = []
      #print(str(clusterCentroidArray[minimumIdx]) + " x = " + str(clusterCurrentTotalSumsCoordinates[minimumIdx][0]))
      #print(str(clusterCentroidArray[minimumIdx]) + " y = " + str(clusterCurrentTotalSumsCoordinates[minimumIdx][1]))
  

def calculateCentroids2():
  for index, item in enumerate(clusterCentroidArray):
    x = clusterCurrentTotalSumsCoordinates[index][0]/clusterCurrentTotalPointsArray[index]
    y = clusterCurrentTotalSumsCoordinates[index][1]/clusterCurrentTotalPointsArray[index]
    clusterCentroidArray[index] = [x, y]
  print(clusterCentroidArray)  

def ResetClusters():
  clusterCurrentTotalPointsArray = []
  for i in values:
    clusterCurrentTotalPointsArray.append(0)
  print("dont stop")

      
'''
totalDis = 0
totalPoints = 0
totalSum = 0
print(clusterCurrentTotalSums)
print(clusterCurrentTotalPointsArray)
print(clusterCurrentTotalPointsArray)
for index, item in enumerate(clusterCentroidArray):
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
  clusterCentroidArray[index] = [x, y]
inTheLoop = compareList(clusterCurrentTotalPointsArray, clusterPreviousTotalPointsArray)
if(inTheLoop):
    clusterPreviousTotalPointsArray = clusterCurrentTotalPointsArray
    clusterCurrentTotalPointsArray = []
    for i in values:
      clusterCurrentTotalPointsArray.append(0)
    print("dont stop")
else:
    print("stop")
print(clusterCentroidArray)
'''

a= [4, 5, 6, 6, 7]
print(a)
a =[]
print(a)
for i in values:
  a.append(0)
print(a)


assignCoords()
calculateCentroids2()
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
    print("before current clusters points = " + str(clusterCurrentTotalPointsArray))
    print("before previous clusters points = " + str(clusterPreviousTotalPointsArray))
    clusterPreviousTotalPointsArray = clusterCurrentTotalPointsArray
    print("after current clusters points = " + str(clusterCurrentTotalPointsArray))
    print("after previous clusters points = " + str(clusterPreviousTotalPointsArray))
    clusterCurrentTotalPointsArray = []
    clusterCurrentTotalSumsCoordinates = []
    clusterCurrentTotalSums = []

    for i in values:
      clusterCurrentTotalPointsArray.append(0)
      clusterCurrentTotalSums.append(0)
      clusterCurrentTotalSumsCoordinates.append([0,0])

    print("after2 current clusters points = " + str(clusterCurrentTotalPointsArray))
    assignCoords()
    calculateCentroids2()
 
  

  
   
  

  
  