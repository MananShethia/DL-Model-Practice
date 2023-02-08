#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:15:19 2023

@author: spaul
"""

from osgeo import gdal
import matplotlib.pyplot as plt
import numpy as np

#%%
mask_img = gdal.Open('/data/manan/38-Cloud Dataset/Forest/BC/LC81800662014230LGN00/LC81800662014230LGN00_fixedmask.img')
b4_tif = gdal.Open('/data/manan/38-Cloud Dataset/Forest/BC/LC81800662014230LGN00/LC81800662014230LGN00_B4.TIF')


tif_geot = b4_tif.GetGeoTransform()
img_proj = b4_tif.GetProjection()
img_geot = (tif_geot[0], tif_geot[1], 0, tif_geot[3], 0, tif_geot[5])
tif_file = gdal.GetDriverByName("GTiff").Create("/data/manan/38-Cloud Dataset/Forest/BC/LC81800662014230LGN00/LC81800662014230LGN00_fixedmask.TIF", mask_img.RasterXSize, mask_img.RasterYSize, mask_img.RasterCount, mask_img.GetRasterBand(1).DataType)
print(mask_img.RasterXSize, mask_img.RasterYSize, mask_img.RasterCount, mask_img.GetRasterBand(1).DataType)
tif_file.SetProjection(img_proj)
tif_file.SetGeoTransform(img_geot)

#print(img_geot, tif_geot)

#%%
for i in range(mask_img.RasterCount):
    band = mask_img.GetRasterBand(i + 1)
    tif_file.GetRasterBand(i + 1).WriteArray(band.ReadAsArray())

tif_file.FlushCache()
tif_file=None

print(mask_img, b4_tif, tif_file)

print("--------------------")

#%%
# READ THE BANDS AS NUMPY ARRAY
b1 = mask_img.ReadAsArray()
b2 = b4_tif.ReadAsArray()
#b3 = tif_file.ReadAsArray()
#print( b1, b2)
print(b1.max(), b1.min())
print(b2.max(), b2.min())
#print(b3.max(), b3.min())
# PUTTING THE ARRAY USING IMSHOW()
#b2 = np.moveaxis(b2, 0, 2)
print(b1.shape, b2.shape)
#plt.figure()
#plt.imshow(b1, cmap="gray")
#plt.figure()
#plt.imshow(b2, cmap="gray")
#plt.figure()
#plt.imshow(b3, cmap="gray")
#plt.savefig("forest1.png")
#plt.show()

print("----------------------------")
#%%
new_tif = gdal.Open("/data/manan/38-Cloud Dataset/Forest/BC/LC81800662014230LGN00/LC81800662014230LGN00_fixedmask.TIF")
print(new_tif)
b = new_tif.ReadAsArray()
print(b, b.max(), b.min(), b.shape)
plt.figure()
plt.imshow(b, cmap="gray")
plt.show()
