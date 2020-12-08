import csv
import statistics
import pandas as pd

def getTSMedian(listClusterTS):
    tsMedian = []
    j = 0
    flag = 0
    while flag == 0:
        app = []
        for item in listClusterTS:
            if len(item) > j:
                app.append(item[j])
        if len(app) != 0:
            tsMedian.append(statistics.mean(app))
            j += 1
        else:
            flag = 1
    return tsMedian


def adaptTimeSeries(path):
    with open(path, 'r') as csvFile:
        reader = csv.reader(csvFile)
        id = 0
        listOfValue = []
        listOfId = []
        listOfTime = []
        listOfClass = []
        listGeneric = []
        listForDTW = []
        startPoint = 1
        splitClass = 0


        for row in reader:
            listValueApp = []
            # print(row)
            splitted = row[0].split('\t')

            if "AsphaltObstacles" in path or "AsphaltRegularity" in path:
                splitClass = len(splitted) - 1
                startPoint = 0

            listOfClass.append(splitted[splitClass])
            for i in range(startPoint,len(splitted)):
                if splitted[i] != "NaN":
                    listOfValue.append(float(splitted[i]))
                    listValueApp.append(float(splitted[i]))
                    listOfTime.append(i)
                    listOfId.append(id)
                    listGeneric.append((id,i,(float(splitted[i]))))
            listForDTW.append(listValueApp)
            id += 1

        df = pd.DataFrame(listGeneric, columns=['id', 'time','value'])
        series = pd.Series((i for i in listOfClass))


        return df,series,listOfClass,listForDTW



def getDataframeAcc(appSeries,perc):
    listClassExtr = list(appSeries.drop_duplicates())
    series = appSeries
    dictIndexAcc = {}
    dictIndexNotAcc = {}
    # print(listClassExtr)
    # print(series)
    allAccInd = []
    allNotAccInd = []
    for x in listClassExtr:
        sommaClasse = sum(list(series.str.count(x)))
        accepted = int(sommaClasse * perc)
        listIndexAccepted = []
        listIndexNotAccepted = []
        for i in range(len(series)):
            if series[i] == x:
                if len(listIndexAccepted) <= accepted:
                    listIndexAccepted.append(i)
                    allAccInd.append(i)
                else:
                    listIndexNotAccepted.append(i)
                    allNotAccInd.append(i)
    return list(sorted(allAccInd)),list(sorted(allNotAccInd))



def extractFeature(listOut, series,trainFeatDataset):
    allAcc,allNotAcc = getDataframeAcc(series,trainFeatDataset)
    dictSeed = {}
    for index in allAcc:
        if not series[index] in dictSeed.keys():
            listTSAcc = []
        else:
            listTSAcc = dictSeed[series[index]]
        listTSAcc.append(list(listOut[listOut.id==index].value))
        dictSeed[series[index]] = listTSAcc

    return dictSeed

def getCentroid(dictSeed):
    listCentr = []
    for key in dictSeed.keys():
        listCentr.append(getTSMedian(dictSeed[key]))
    return listCentr



def castTimeSeries(listOut):

    if not type(listOut) == list:
        idList = list(set(list(listOut.id)))
    else:
        idList = range(len(listOut))

    listTimeSeriesCasted = []
    for i in idList:
        if not type(listOut) == list:
            listApp = list(listOut[listOut.id==i].value)
        else:
            listApp = listOut[i]
        listCast = []
        for val in listApp:
            listCast.append([val])
        listTimeSeriesCasted.append(listCast)
    return listTimeSeriesCasted
