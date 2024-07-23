# %%
# from ./data/LWI_NOAA_BC_Lines.shp, get each USGS gage number from the name and write to a .txt file
import os
import geopandas as gpd

#open the shapefile in ./data
shp = gpd.read_file(r'.\data\LWI_NOAA_BC_Lines.shp')
# add a new column to the dataframe to hold the USGS gage number
shp['USGS'] = shp['Name'].str.extract(r'(\d{8})')
shp

# %%
# write the USGS station file using hte following example text
# USGS Data Retrieval: Instantaneous

# Station Name=10_08041300
# Stream Name=
# Station ID=08041300
# Version Name=USGS
# Latitude=
# Longitude=
# Elevation=
# Coord Datum=
# Available Peak Start=30Dec2018
# Available Daily Start=14Jun2018
# Available Daily End=15Jul2024
# Available Instantaneous Start=13Jun2018
# Available Instantaneous End=16Jul2024

# Station Name=33_08033500
# Stream Name=
# Station ID=08033500
# Version Name=USGS
# Latitude=
# Longitude=
# Elevation=
# Coord Datum=
# Available Peak Start=04Oct1923
# Available Daily Start=01Jul1903
# Available Daily End=15Jul2024
# Available Instantaneous Start=01Oct2007
# Available Instantaneous End=16Jul2024

# Create an example based on first row of shp
with open(r'.\data\USGS.txt', 'w') as f:
    f.write('USGS Data Retrieval: Instantaneous\n')
    f.write(f'Station Name={shp["Name"][0]}\n')
    f.write(f'Stream Name=\n')
    f.write(f'Station ID={shp["USGS"][0]}\n')
    f.write(f'Version Name=USGS\n')
    f.write(f'Latitude=\n')
    f.write(f'Longitude=\n')
    f.write(f'Elevation=\n')
    f.write(f'Coord Datum=\n')

# %%
# write the USGS gage numbers to a .txt file
with open(r'.\data\USGS.txt', 'w') as f:
    for i in range(len(shp)):
        f.write('USGS Data Retrieval: Instantaneous\n')
        f.write(f'Station Name={shp["Name"][i]}\n')
        f.write(f'Stream Name=\n')
        f.write(f'Station ID={shp["USGS"][i]}\n')
        f.write(f'Version Name=USGS\n')
        f.write(f'Latitude=\n')
        f.write(f'Longitude=\n')
        f.write(f'Elevation=\n')
        f.write(f'Coord Datum=\n')
        f.write(f'\n')
# %%
