import csv
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster import hierarchy
from scipy.spatial.distance import pdist
KVALUE = 4

with open('clusteringData.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

allPointsList = []
for item in texts:
	allPointsList.append((float(item[0]),float(item[1])))
allPointsListNp=np.array(allPointsList)
Z = hierarchy.linkage(allPointsListNp, 'single', metric='euclidean')

fl = hierarchy.fcluster(Z,KVALUE,criterion='maxclust')
zipList = list(zip(fl,allPointsListNp))


plt.plot([x[1][0] for x in zipList if x[0]==1],[x[1][1] for x in zipList if x[0]==1], 'bo',
	[x[1][0] for x in zipList if x[0]==2],[x[1][1] for x in zipList if x[0]==2], 'go',
	[x[1][0] for x in zipList if x[0]==3],[x[1][1] for x in zipList if x[0]==3], 'mo',
	[x[1][0] for x in zipList if x[0]==4],[x[1][1] for x in zipList if x[0]==4], 'ro',
	)


plt.show()