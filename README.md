
# Analyzing Residential Property by Zip Code

## Summary

This analysis uses parcel-level property tax data from New York State to explore residential property values by zip code in Onondaga County. It also introduces plotting via the matplotlib module.

## Input Data

The input data is a file called **onondaga-tax-parcels.zip** that will need to be downloaded from the course Google Drive folder. It *does not* need to be unzipped: you'll read the data from it directly using Pandas. If you want to see what's in it, the first few lines are available in `firstlines.csv` in the Google Drive folder.

The zip file contains a single large CSV file called `onondaga-tax-parcels.csv`. That file has one record (line) for every parcel of land in Onondaga County. It is derived from the New York State master database for the county but some fields have been removed to make the file smaller. There are a bit more than 180,000 parcels in total and just over 144,000 of them are residential.

Each of the records has 20 fields (columns). The ones we'll use are: "TOTAL_AV", the total assessed value of the parcel in dollars (it's the sum of the values of the land itself and the buildings on it); "SQFT_LIV", the size of the living area in square feet; "NBR_BEDRM", the number of bedrooms; "YR_BLT", the year the house was built; "CALC_ACRES", the size of the property in acres; "PROP_CLASS", which indicates the classification of the parcel as agricultural, commercial, residential, or various other categories; and "ZCTA5CE10", which is the 5-digit zip code for the property. ZCTA5 is a US Census designation that stands for "zip code tabulation area at the 5-digit level" and CE10 indicates that the zip code boundaries correspond to those that were in place during the 2010 census. 

## Deliverables

A script called **parcels.py** that goes through the steps below. It will produce a figure and a CSV file called `parcels.csv` with summary information about residential housing in each zip code in the county. You'll also submit a short Markdown file called **results.md** with some observations about the results.

