# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 16:36:46 2021

@author: Ali
"""

import matplotlib.pyplot as plt
from pydicom import dcmread
import os
import numpy as np
import pandas as pd
from PIL import Image
from os.path import exists


folder = "./adc_images_sick_dicom/"

error_files=0
files = os.listdir(folder)
for file in files:
    
    try:
        ds = dcmread(folder+file,force=True)
        ds.decompress
        arr = ds.pixel_array

        # arr=arr.astype(np.uint8)
        img=arr
        # img1 = img/np.max(img)
        # if arr.dtype=='uint16':
        img = np.asarray(img)
        img = np.uint8(((img/img.max())*255))
        # else:
            # raise ValueError('image not uint16.')
    except:
        print("error file")
        error_files+=1
        continue
    

    
    # plt.imsave(fname=folder+"converted_images/"+file[:-4]+".png",arr=arr)
    im = Image.fromarray(img)
    fname="./converted_images/"+file[:-4]+".png"
    if not exists(fname):
        plt.imshow(img, cmap="gray")
        plt.show()
        im.save(fp=fname,arr=arr)
print("error_files:", error_files)