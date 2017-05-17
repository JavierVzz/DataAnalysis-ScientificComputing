# Javier Vazquez
# Final Project
# Date: May 16 ,2017
import os
import dataWranglerClass
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class histogramAdult():

    def __init__(self):
        pass

    def plotHistLevel2(self, data, labels):
        colors = patches = []
        ax = plt.subplot()
        if len(labels[1]) > 1:
            dw = dataWranglerClass.dataWrangler()
            file = "ColorsHTML.xlsx"
            sheet = "Colors"
            cols = "B"
            skip = 0
            colorHTML = dw.loadData(file, sheet, cols, skip)
            colors = [colorHTML[i][0] for i in range(len(labels[1]))]
            colors *= 2
            patches = [mpatches.Patch(color=colors[i], label=labels[1][i]) for i in range(len(labels[1]))]
        plt.legend(handles=patches)
        ax.hist(data, color=colors, rwidth=1, align="mid", bins=len(data))
        maxY = max([len(datum) for datum in data])
        i = 1
        for datum in data:
            if datum.size == 0:
                plt.text(i, 0, 0, fontsize=14, horizontalalignment='center',verticalalignment='center')
            else:
                plt.text(datum[0], datum.size+100, datum.size, fontsize=14, horizontalalignment='center',verticalalignment='center')
            i += 1
        p = mpatches.Rectangle((0, 0), (len(data)/2)+.5, maxY+500, facecolor="y", alpha=.2)
        q = mpatches.Rectangle(((len(data)/2)+.5, 0), len(data)/2, maxY+500, facecolor="g", alpha=.2)
        ax.add_patch(p)
        ax.add_patch(q)
        plt.text(len(data)/4+.5, maxY+100, labels[0][0], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='y'))
        plt.text(len(data)*.75+.25, maxY+100, labels[0][1], fontsize=15, horizontalalignment='center', verticalalignment='center',bbox=dict(facecolor='g'))
        ax.set_xticks([i for i in range(1, len(data)+1)])
        ax.set_ylim(0, maxY+500)
        xticks = [label for label in labels[1]]
        xticks *= 2
        ax.set_xticklabels(xticks, rotation='vertical')
        plt.show()

if __name__ == '__main__':
    print("Direct access to " + os.path.basename(__file__))
else:
    print(os.path.basename(__file__) + " class instance")