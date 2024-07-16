#%%
# Create Ref lines from a shp file
# The projection will match the one used in the shp file
import os
import geopandas as gpd

#open the shapefile in ./data
shp = gpd.read_file(r'.\data\LWI_NOAA_BC_Lines.shp')
shp

# %%
# Create a function to write a refLine to a .g## file
def writeRefLine(refLine, filename):
    with open(filename, 'a+') as f:
        for key, value in refLine.items():
            if key == 'Ugly Ends':
                f.write(f'{value}\n')
            else:
                f.write(f'{key}={value}\n')
# %%
# create a for loop to write all the refLines to a single .g## file
for i in range(len(shp)):
    refLine = {
        'Reference Line Name': shp['Name'][i],
        'Reference Line Storage Area': 'Model_Domain',
        'Reference Line Start Position': f'{shp.geometry[i].coords[0][1]} , {shp.geometry[i].coords[0][0]}',
        'Reference Line Middle Position': f'{shp.geometry[i].centroid.coords[0][1]} , {shp.geometry[i].centroid.coords[0][0]}',
        'Reference Line End Position': f'{shp.geometry[i].coords[1][1]} , {shp.geometry[i].coords[1][0]}',
        'Reference Line Arc': '2',
        'Ugly Ends': f'{shp.geometry[i].coords[0][1]}{shp.geometry[i].coords[0][0]}{shp.geometry[i].coords[1][1]}{shp.geometry[i].coords[1][0]}',
        'Reference Line Text Position': '1.79769313486232E+308 , 1.79769313486232E+308',
        'Reference Point Name': shp['Name'][i],
        'Reference Point Position': f'{shp.geometry[i].coords[1][0]} , {shp.geometry[i].coords[1][1]}'
    }
    writeRefLine(refLine, r'.\data\refLine.g00')