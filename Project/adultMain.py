# Javier Vazquez
# Final Project
# Date: May 16 ,2017
# Source: http://archive.ics.uci.edu/ml/datasets/Adult

import os
import dataWranglerClass, histogramClass

def main():

    #url for the training data for the linear classifier
    url = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

    dw = dataWranglerClass.dataWrangler()
    hc = histogramClass.histogramAdult()

    # file = "project_data.xlsx"
    # sheet = "data"
    # cols = "A:O"
    # skip = 0
    # data = dw.loadData(file, sheet, cols, skip)

    # Get the data from internet without manual download
    # data is a pandas dataframe
    data = dw.getData(url)

    # Pandas data frame to numpy ndarray
    data = data.values

    # 1: workclass 9
    # 3: education 16
    # 5: marital 7
    # 6: occupation 15
    # 7: relationship 6
    # 8: race 5
    # 9: sex 2
    # 13: country 42
    # 14: income
    index = [1,3,5,6,7,8,9,13,14]

    for i in index:
        labels, aspect = dw.sortDataPerLabels(data, 14, i)
        aspectToPlot = dw.convertDataPerLabel(aspect)
        hc.plotHistLevel2(aspectToPlot, labels)

if __name__ == '__main__':
    print(os.path.basename(__file__))
    main()