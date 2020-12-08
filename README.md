# TimeSeriesSeedingKMeans
In this repository I've implemented the Semi Supervised Time Series Clustering called Seeded kMeans using the DTW as distance. The reference paper for this code is: *Basu, S., Banerjee, A., & Mooney, R. (2002). Semi-supervised clustering by seeding. In Proceedings of 19th International Conference on Machine Learning (ICML-2002).*

## Input File

In input are accepted only .tsv files, where each row represents the time series and the first column represents the label of the time series. Each point of the time series is separated by  a tab (\t).
All the .tsv files should be inside a folder with the same name of the file.

## Parameters

The algorithm requires only the percentage of the number of labels to use in order to start the computation. It is possible to modify the percentage via the *trainFeatDataset* variable.

## Issues

At the moment, the code doesn’t accept time series with different length. It will be fixed ASAP.




