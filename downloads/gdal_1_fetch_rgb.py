#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:15:19 2023

@author: spaul
"""

from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

try:
    gdalImg()
except:
    print("Image doen't exist")

print("Hello World!!!")


def gdalImg():
    dataset = gdal.Open('/data/manan/38-Cloud Dataset/Forest/BC/LC80070662014234LGN00/LC80070662014234LGN00_B2_RGB.bmp')

    print(dataset.RasterCount) # PRINT NUMBER OF BANDS IN THAT IMAGE
    
    # TO FETCH INDIVIDUAL BANDS
    band1 = dataset.GetRasterBand(1)
    band2 = dataset.GetRasterBand(2)
    band3 = dataset.GetRasterBand(3)
    
    # READ THE BANDS AS NUMPY ARRAY
    b1 = band1.ReadAsArray()
    b2 = band2.ReadAsArray()
    b3 = band3.ReadAsArray()
    
    # PUTTING THE ARRAY USING IMSHOW()
    img = np.dstack((b1, b2, b3))
    f = plt.figure()
    plt.imshow(img)
    #plt.savefig("forest1.png")
    plt.show()