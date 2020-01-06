#!/usr/bin/python
import matplotlib.pyplot as plt
import random
import numpy as np
import statisticsOfData as stats
import importAndCleanData as dataCleaning
import matplotlib.pyplot as plt 
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

# We got the right data in cleanedData
cleanedData = dataCleaning.fillMissingValuesAndNormalizeData()

# reduced dimensions
reducedDimension = 30

# maximum value for k
kmax = 25

# WSS - within cluster sum of the squared errors
wss = [0 for i in range(kmax)] 


def findMinDistanceBetweenCenterAndPoints(centers, i, k, cleanedData, clusterResult):
	squaredDistance = [0 for m in range(len(centers))]
	# point is i and the center is center[j]
	min=999
	m=0
	for j in centers:
		for l in range(0, reducedDimension):
			squaredDistance[m] += ((cleanedData[j][l]-cleanedData[i][l])**2)
		if(min > squaredDistance[m]):
			min = squaredDistance[m]
			clusterResult[i] = j
		m+=1
	wss[k] += min

def kmeansImplementation(cleanedData):
	# implementation of k means
	clusterResult = [0 for n in range(527)]
	for k in range(1, kmax):
		centers = [0 for i in range(k)]
		for j in range(0, k):
			# finding k random centers
			centers[j] = random.randint(0,526)
		
		# We got now k centers
		for i in range(0,527):
			findMinDistanceBetweenCenterAndPoints(centers, i, k, cleanedData, clusterResult)

	graphOfWSSVsK(wss)
	
	return clusterResult

# The Silhouette Method for finding the optimal value of k
def silhouetteMethod(cleanedData):
	sil = []
	 # Silhouette score for 0 and 1 is zero so appending 0 for 0th and 1st location
	sil.append(0)
	sil.append(0)
	# dissimilarity would not be defined for a single cluster, thus, minimum number of clusters should be 2
	for k in range(2, kmax):
	  kmeans = KMeans(n_clusters = k).fit(cleanedData)
	  labels = kmeans.labels_
	  sil.append(silhouette_score(cleanedData, labels, metric = 'euclidean'))
	silhouetteGraph(sil)
	return sil

def graphOfWSSVsK(wss):
	# graph of k and wss values
	x = [0 for i in range(kmax)]
	for i in range(0, kmax):
		x[i] = i

	y = [0 for i in range(kmax)]
	for i in range(0, kmax):
		y[i] = wss[i]

	plt.plot(x, y) 
	  
	# naming the x axis 
	plt.xlabel('k values') 
	# naming the y axis 
	plt.ylabel('wss values') 
	  
	# giving a title to my graph 
	plt.title('k vs wss') 
	  
	# function to show the plot 
	plt.show() 


# Contains the sillhouette scores
def silhouetteGraph(sil):
	# Silhouette graph
	xs = [0 for i in range(kmax)]
	for i in range(2, kmax):
		xs[i] = i

	plt.plot(xs, sil) 
	  
	# naming the x axis 
	plt.xlabel('k values') 
	# naming the y axis 
	plt.ylabel('sillhouette scores') 
	  
	# giving a title to my graph 
	plt.title('k vs sillhouette scores') 
	  
	# function to show the plot 
	plt.show() 


optimalValueOfk = 0;

def findMaxValueOfK(sil):
	# Now finding the maximum value of the array ys, containing all the Silhouette scores
	max = 0
	for i in range(0, len(sil)):
		if(max < sil[i]):
			max = sil[i]
			optimalValueOfk = i

	print("\n\n\nThe optimal value of k by Silhouette method is : "+str(optimalValueOfk))

	print("\nAgain finding the cluster analysis for optimal no of the clusters, k = "+str(optimalValueOfk))

	return optimalValueOfk


def clusteringForOptimalK(optimalValueOfk):
	# Clustering again for optimal Value Of k
	centers = [0 for i in range(optimalValueOfk)]

	print("\noptimal value of k :"+str(optimalValueOfk))

	for j in range(0, optimalValueOfk):
		# finding k random centers
		centers[j] = random.randint(0,526)
		
	clusterResult = [0 for n in range(527)]

	# We got now k centers		
	for i in range(0,527):
		findMinDistanceBetweenCenterAndPoints(centers, i, optimalValueOfk-1, cleanedData, clusterResult)

	return clusterResult

def renamingTheClusters(finalCluster):
	# Renaming the cluster to 1,2,3,4....
	renamedClusterNumber = 1
	dict = {}
	print("\nPoint number  Cluster number")
	for i in range(0,527):
		if finalCluster[i] in dict:
			print(str(i+1)+"\t\t"+str(dict[finalCluster[i]]))
		else:
			dict[finalCluster[i]] = renamedClusterNumber
			renamedClusterNumber += 1
			print(str(i+1)+"\t\t"+str(dict[finalCluster[i]]))

clusterResult = kmeansImplementation(cleanedData)
sil = silhouetteMethod(cleanedData)
optimalValueOfk = findMaxValueOfK(sil)
finalCluster = clusteringForOptimalK(optimalValueOfk)
renamingTheClusters(finalCluster)
