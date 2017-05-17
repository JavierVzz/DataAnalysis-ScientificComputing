# Javier Vazquez
# Final Project
# Date: May 16 ,2017
import os
import pandas as pd
import numpy as np

class dataWrangler():

    def __init__(self):
        pass

    def loadData(self, file, sheet, cols, skip):
        """Load an excel file to df"""
        df = pd.read_excel(io=file, sheetname=sheet, header=0, parse_cols=cols, skiprows=skip).values
        return df

    def getData(self, url):
        """Gets the data from the specified URL"""
        data = pd.read_csv(url, header=None)
        return data
    
    def sortDataPerLabels(self, data, *args):
        labels = [np.unique(data[:,arg]) for arg in args]
        income = [data[np.where(data == label), :] for label in labels[0]]
        countPerLabel = [income[i][0][np.where(income[i][0] == labels[1][j]), :] for i in range(len(labels[0])) for j in range(len(labels[1]))]
        return labels, countPerLabel

    def convertDataPerLabel(self, data):
        listLabel = [np.ones(len(data[i][0]))*(i+1) for i in range(len(data))]
        return listLabel

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")