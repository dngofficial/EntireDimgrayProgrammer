import random
import math

checking_points = []
with open('coordinates.csv', 'r') as file:
  for line in file:
    point = line.split(',')
    for index, item in enumerate(point):
      point[index] = float(item)

    checking_points.append(point)

clust = int(input("Enter your number of clusters: "))
random_centers = random.sample(checking_points, clust)

# checking_points = checking_points.copy()
for item in random_centers:
  checking_points.remove(item)

for item in checking_points:
  item.append(clust + 2)
  item.append(21)

print(random_centers[0])

print(random_centers[1])
global changed_points
changed_points = 0


def find_points():
  for item in checking_points:
    distances = []
    for center in random_centers:
      #print("item = " + str(item))
      #print(center)
      dist = math.dist(item[0:2], center[0:2])
      distances.append(dist)

    smallest = min(distances)
    index = distances.index(smallest)
    if smallest == 0:
      index = random_centers.index(item)

    if (index != item[2]):
      global changed_points
      changed_points += 1

    item[2] = index
    item[3] = smallest


find_points()

for center in random_centers:
  center.append(random_centers.index(center))
  center.append(0)
  checking_points.append(center)

print(checking_points[0])

global total_distance
total_distance = 0


def find_distance():
  global total_distance
  total_distance = 0
  for item in checking_points:
    dist_squ = item[3]**2
    total_distance += dist_squ


def find_clusters():
  for c in range(clust):
    clust_dist = 0
    clust_points = 0
    clust_x = 0
    clust_y = 0
    for item in checking_points:
      if c == item[2]:
        clust_dist += item[3]
        clust_points += 1
        clust_x += item[0]
        clust_y += item[1]

    new_x = clust_x / clust_points
    new_y = clust_y / clust_points
    random_centers[c] = [new_x, new_y]
    print(random_centers[c])


find_clusters()

print(changed_points)

while (changed_points != 0):
  changed_points = 0
  find_points()
  find_distance()
  print('distance: ' + str(total_distance))
  find_clusters()
  print(changed_points)
