#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 11:51:09 2023

@author: anano
"""

import pandas as pd
import matplotlib.pyplot as plt

use_type = {"ZCTA5CE10":str} #specifies data type of ZCTA5CE10 (zip code for property) as string
raw = pd.read_csv("onondaga-tax-parcels.zip", dtype=use_type) #tells python to interpret ZCTA column as string
len(raw) #it has 180704 records

raw["zipcode"] = raw["ZCTA5CE10"] #duplicates ZCTA to zipcode
raw["value_k"] = raw["TOTAL_AV"]/1000 #changes reporting unit to thousands of dollars

key_vars = ["zipcode", "value_k", "PROP_CLASS"]
usable = raw.dropna(subset=key_vars)#drops missing values from key_vars
len(usable) #it has 180450 records

is_res = usable["PROP_CLASS"].between(200, 299) #marks residential properties TRUE

res = usable[is_res] #res stores values which are true (e.i. values about residential properties)
len(res)

tot_n = len(res) #total_n equals to number of records in res
mean_k = res["value_k"].mean() #when attempting to round, error occurs: 'float' object has no attribute 'round'
tot_bil = (res["value_k"].sum())/1e6 #calculates total value of property in billions

print("Number of Records: ", tot_n)
print("Average Value of Property: ", mean_k)
print("Total Value of Propoerty: ", mean_k)

by_zip = res.groupby("zipcode") #groups data by zipcode
attr = ["SQFT_LIV", "NBR_BEDRM", "YR_BLT", "CALC_ACRES"]
summary = by_zip[attr].median()
print(summary) #reult is dataframe that gives median size of living area, # of bedrooms and year of construction 
# by zipcode
summary = summary.round(2)
summary = summary.sort_values("YR_BLT")
print(summary)

value = by_zip["value_k"].describe() #displays summary statistics about propoerty values
value = value.round(2)
value = value.sort_values("50%")
print(value) 

for c in value.columns: 
    summary[c] = value[c]
#use a for loop to loop over the columns of value. 
#Within the loop, we set the summary column c to the value column c using the assignment operator =. 
#Since summary and value have the same index (the zip codes), this will effectively merge the data from value into summary.

summary = summary.sort_index()
summary.to_csv("parcels.csv") #write the results to the output file

fig1, ax1 = plt.subplots() #create new blank figure, fig1 and set of axes, ax1
summary.plot.scatter("YR_BLT", "SQFT_LIV", s='50%', ax=ax1)
title = ax1.set_title("Characteristics of Zip Codes")
fig1.tight_layout()
fig1.savefig("parcels.png", dpi=300)
