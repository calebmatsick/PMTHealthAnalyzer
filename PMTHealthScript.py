# All needed imports
import os
import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path


# Driver method for the script
def main():
    dirPath = input('What directory are the value files in?')

    pathlist = Path(dirPath).rglob('*')
    for path in pathlist:
        strPath = str(path)        


# Check for main
if __name__ == '__main__':
    main()