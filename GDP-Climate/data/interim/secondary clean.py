# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 19:33:42 2026

@author: Geraint
"""

import pandas as pd 

gdpdf = pd.read_excel(open('C:/Users/Geraint/Desktop/Project 1/mpd2023_web.xlsx','rb'), sheet_name=3)

gdpdf.head()

#A lot of NaN data will replace with 0 

gdpdf1 = gdpdf.fillna(0)

gdpdf1.head()

#NaN has been replaced

