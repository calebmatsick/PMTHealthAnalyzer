# All needed imports
import os
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


NUMTUBES = 55


# Driver method for the script
def main():
    dirPath = input('What directory are the value files in?\n')

    mainArray = np.zeros((1, NUMTUBES, 4))

    fileWalk = next(os.walk(dirPath))[2]
    numFiles = len(fileWalk)

    pathlist = Path(dirPath).rglob('*')
    for path in pathlist:
        strPath = str(path)        
        dataFrame = np.loadtxt(strPath, skiprows=1 + 57, dtype=int)

        mainArray = np.vstack(dataFrame, mainArray)

    x = np.arrange(1, numFiles)

    for i in range(1, NUMTUBES + 1):

        courseVals = []
        for i in range(1, numFiles):
            courseVals.append(mainArray(i, i, 2))

        plt.title("Tube" + i + " - Course Grain")
        plt.xlabel("Reading 1-" + numFiles)
        plt.ylabel("Course Grain")
        plt.plot(x, color = "green")
        plt.show()


# Check for main
if __name__ == '__main__':
    main()