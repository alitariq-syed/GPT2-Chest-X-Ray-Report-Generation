# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 11:30:19 2021

@author: Ali
"""
import pandas as pd
import shutil
import os
from os.path import exists


data = pd.read_csv('CR_selected_dataaa_updated.csv')

image_paths = data['Image Index']


row=0
for path in image_paths:
    
    data.at[row,'Image Index'] = path[:-4]+".png"
    row+=1
    
data.to_csv('CR_selected_dataaa_updated_renamed_files.csv')