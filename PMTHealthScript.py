# All needed imports
import os
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# Driver method for the script
def main():
    dirPath = input('What directory are the value files in?')

    mainArray = np.zeroes((1, 55, 4))

    pathlist = Path(dirPath).rglob('*')
    for path in pathlist:
        strPath = str(path)        
        dataFrame = np.loadtext(strPath, skiprows=1 + 57, dtype=int)

        mainArray = np.vstack(dataFrame, mainArray)
# Check for main
if __name__ == '__main__':
    main()