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
# #selected cases:
# tb_cases = [965,966,1874,1982]
# covid_cases = [21,761,1669,3182]

# #readCSV
# selectedData = pd.read_csv("selectedData.csv",index_col=0)

# tb_data = selectedData.loc[selectedData['Unnamed: 0.1'].isin(tb_cases)]
# covid_cases = selectedData.loc[selectedData['Unnamed: 0.1'].isin(covid_cases)]


folder = "./adc_images/"
# folder = "./SelectedImages/possible covid"

files = os.listdir(folder)
for file in files:
    
    try:
        ds = dcmread(folder+file,force=True)
        arr = ds.pixel_array
        
        arr = arr/arr.max()
        arr = (arr * 255.0)
        arr=arr.astype(np.uint8)
    except:
        continue
    
    # plt.imshow(arr, cmap="gray")
    # plt.show()
    
    # plt.imsave(fname=folder+"converted_images/"+file[:-4]+".png",arr=arr)
    im = Image.fromarray(arr)
    im.save(fp=folder+"converted_images/"+file[:-4]+".png",arr=arr)
    