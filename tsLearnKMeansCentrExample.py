from tslearn.clustering import TimeSeriesKMeans
import meanTimeSeries as util
import numpy as np
from sklearn.metrics import adjusted_rand_score,accuracy_score,adjusted_mutual_info_score


nameDataset = "Coffee"
trainFeatDataset = 0.2
testPath = "./" + nameDataset + "/" + nameDataset + ".tsv"
listOut, series,listOfClass, listForDTW = util.adaptTimeSeries(testPath)
seedTS = util.extractFeature(listOut, series,trainFeatDataset)
print("Class Found: " + str(len(seedTS.keys())))
centroid = util.getCentroid(seedTS)
X_train = util.castTimeSeries(listOut)
centroid = util.castTimeSeries(centroid)

listCentr = []
for clust in centroid:
    listCentr.append(clust)


X = np.array(listCentr,np.float64)
model = TimeSeriesKMeans(n_clusters=len(seedTS.keys()), metric="dtw", max_iter=10,init=X)
model.fit(X_train)
groundTruth = [int(i) for i in list(series)]
print("Labels Discovered")
print(list(model.labels_))
print("Original Labels")
print(groundTruth)
print("Adjusted Rand Index")
print(adjusted_rand_score(model.labels_,groundTruth))
