# import gdal
import numpy as np
import os
from skimage import io

dictionary = {
    'Barren': ['1', '2', '3'],
    'Forest': ['1', '2'],
    'shrubland': ['1', '2', '3'],
    'Snow': ['1', '2'],
    'Grass_Crop': ['1'],
    'Water': ['1', '2', '3'],
    'Wetland': ['1', '2', '3'],
}

patches = []
labels = []

path = '/data/manan/38-cloud-dataset/'

for band_range in ['_r', '_g', '_b']:
    for index, (field, field_set) in enumerate(dictionary.items()):
        field_set_len = len(field_set)
        print(index, field, field_set, field_set_len)

        patch_band = []
        label_band = []
        for i in range(field_set_len):
            print(path + field + '/BC/' +
                  field_set[i] + '/{0}'.format(field_set[i]) + band_range + '.tif')
            # ds = gdal.Open(path + field + '/BC/' + field_set[i] + '/{0}'.format(field_set[i]) + band_range + '.tif')
            # arr = ds.ReadAsArray()
            # arr = np.where(arr == 64, 128, arr)
            # arr = np.where(arr == 192, 255, arr)
            # for row in range(0, arr.shape[0], 256):
            #     for col in range(0, arr.shape[1], 256):
            #         patch = arr[row:row+256, col:col+256]
            #         io.imsave('path', patch)

            # path will be for example /... + [red_ , blue_ , green_ , gt_ ] + LC..(name of tiff)
            # also append it to some list

            #         patch_band.append(patch)
            #         if np.mean(patch) <= 128:
            #             label_band.append(0) # Not Cloud
            #         elif np.mean(patch) < 200:
            #             label_band.append(1) # Thin Cloud
            #         else:
            #             label_band.append(2)
            #
            #         Save the patch as a separate image
            #         io.imsave'path', patch)

        # Convert the list of patches to a NumPy array
        # patch_band = np.array(patches)
        # label_band = np.array(labels)

        # np.save("patch_band.npy", patch_band)
        # np.save("label_band.npy", label_band)

    print('--------------\nBAND CHANGE\n---------------')


# def save_patch():
