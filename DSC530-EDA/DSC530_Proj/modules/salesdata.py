"""This file contains code used in BU Data SCience
"""

# from __future__ import print_function, division

# import numpy as np
import pandas as pd
import os

# import thinkplot
# import thinkstats2

# import sys
# sys.path.append('dataset')
# for path in sys.path:
#    print(path)


## print(os.listdir("../dataset"))


def ReadData(filename = "SalesKaggle3.csv"):
   """
    Parameters
    ----------
    filename : TYPE, optional
        DESCRIPTION. The default is "../dataset/SalesKaggle3.csv".

    Returns
    -------
    None.

    """ 
   data = pd.read_csv(filename, skiprows = None)



def main():
    df = ReadData()
    print(df)


if __name__ == "__main__":
    main()


