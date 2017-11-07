import csv
import math
import random
import matplotlib.pyplot as plt
KVALUE = 4
with open('clusteringData.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
"""
allPointsList = []
for item in texts:
	allPointsList.append((float(item[0]),float(item[1])))
"""
allPointsList = []
for item in texts:
	allPointsList.append((float(item[0]),float(item[1])/7))

def euclidean_distance(pointA,pointB):
	return math.sqrt(abs(pointA[0]-pointB[0])**2+abs(pointA[1]-pointB[1])**2)

def clustering(k,CentroidPoint,allPoints):
	#Initiate k point as center points
	#Calculate distance of every points and center points
	#Put these points in the closest cluster
	clusterList = []
	for point_index in range(0,len(allPoints)):
		clusterList.append([(float(allPoints[point_index][0]),float(allPoints[point_index][1]))])
		for CentroidPoint_index in range(0,len(CentroidPoint)):
			clusterList[point_index].append((CentroidPoint_index,euclidean_distance((float(allPoints[point_index][0]),float(allPoints[point_index][1])),(CentroidPoint[CentroidPoint_index][0],CentroidPoint[CentroidPoint_index][1]))))
	newClusteringList = []
	for item in clusterList:
		newClusteringList.append([item[0],min(item[1:k+1],key=lambda x:x[1])]) 
	return newClusteringList


def clustering_classify(initial_cluster):
	#Put points with same index in one cluster
	i = 0
	clusterList = []
	while i < KVALUE:
		clusterList.append([])

		for item in initial_cluster:
			if item[1][0] == i:
				clusterList[i].append(item[0])
		i = i + 1
	return clusterList


def getCentroid(listPoint):

	meanX = sum(x[0] for x in listPoint)/len(listPoint)
	meanY = sum(x[1] for x in listPoint)/len(listPoint)

	def sortKey(x):
		return (math.atan2(x[1] - meanY, x[0] - meanX) + 2 * math.pi) % (2*math.pi)

	listPoint.sort(key=sortKey)


	totalArea = 0
	totalX = 0
	totalY = 0

	listPoint.append(listPoint[0])

	for i in range(0,len(listPoint)-1):
		a = listPoint[i]
		b = listPoint[i+1]

		area =  0.5 * (a[0] * b[1] - b[0] * a[1])
		x = (a[0] + b[0]) / 3
		y = (a[1] + b[1]) / 3

		totalArea += area
		totalX += area * x
		totalY += area * y
	return [totalX / totalArea, totalY/ totalArea]




def checkAssign(before,after):
	if before == []:
		return False 
	return set(before[0])==set(after[0]) 	

def clustering_iteration():
	newCentroid = []
	for item in clusterInitialList:
		newCentroid.append((getCentroid(item)))

	clusterListBefore = []
	clusterList = clusterInitialList
	
	while not checkAssign(clusterListBefore,clusterList) :
		newCentroidIteration = []
		for item in clusterList:
			newCentroidIteration.append((getCentroid(item)))
		clusterListBefore = clusterList			
		clusterList = clustering_classify(clustering(KVALUE,newCentroidIteration,allPointsList))

		
	plt.plot([x[0] for x in clusterList[0]],[y[1] for y in clusterList[0]], 'bo',newCentroidIteration[0][0],newCentroidIteration[0][1],'b*',
		[x[0] for x in clusterList[1]],[y[1] for y in clusterList[1]], 'go',newCentroidIteration[1][0],newCentroidIteration[1][1],'g*',
		[x[0] for x in clusterList[2]],[y[1] for y in clusterList[2]], 'ko',newCentroidIteration[2][0],newCentroidIteration[2][1],'k*',
		[x[0] for x in clusterList[3]],[y[1] for y in clusterList[3]], 'ro',newCentroidIteration[3][0],newCentroidIteration[3][1],'r*',
		)

	plt.show()

	


xList = []
yList = []
for item in allPointsList:
	xList.append(float(item[0]))
	yList.append(float(item[1]))

initiate_points=[
[random.uniform(min(xList),max(xList)), random.uniform(min(yList), max(yList))],
[random.uniform(min(xList),max(xList)), random.uniform(min(yList), max(yList))],
[random.uniform(min(xList),max(xList)), random.uniform(min(yList), max(yList))],
[random.uniform(min(xList),max(xList)), random.uniform(min(yList), max(yList))],
]

initial_clustering = clustering(KVALUE,initiate_points,allPointsList)
clusterInitialList = clustering_classify(initial_clustering)
clustering_iteration()
