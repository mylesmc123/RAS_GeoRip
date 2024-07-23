# To assign Observed DSS data to BC lines in the RAS model, 
# the .u## file needs to be updated to include lines specifying the DSS records assigned to each BC line.
# This script will create the text needed to add to the .u## file based on the BC Lines in a DSS file.

#%%
from pydsstools.heclib.dss import HecDss

# Open the DSS file
dss_file = r'.\data\lwi_coastwide_usgs_refLines.dss'
dss = HecDss.Open(dss_file)
# get the pathnames of the BC lines
pathnames = dss.getPathnameList("/*/*/FLOW/*/*/*/")
pathnames
# %%
# use lists comprehension to remove the data part of each pathname
pathnamesnoDpart = []
for pathname in pathnames:
    split = pathname.split('/')
    aPart = split[1]
    bPart = split[2]
    cPart = split[3]
    ePart = split[5]
    fPart = split[6]
    pathnamesnoDpart.append(f'/{aPart}/{bPart}/{cPart}//{ePart}/{fPart}/')
pathnamesnoDpart = list(set(pathnamesnoDpart))
pathnamesnoDpart.sort()
pathnamesnoDpart
# %%
# create the text to add to the .u## file based on the following example text:
# Observed Time Series=Flow|TS Name=BC Line: 10_08041300
# Observed Time Series=Flow|TS Used=-1
# Observed Time Series=Flow|TS Source=DSS
# Observed Time Series=Flow|TS DSS Filename=.\DSS_Input_Files\lwi_coastwide_usgs_refLines.dss
# Observed Time Series=Flow|TS DSS Pathname=//10_08041300/FLOW/13JUN2018/IR-DAY/USGS/
# Observed Time Series=Flow|TS Table Mode=0
# Observed Time Series=Flow|TS Table Use Fixed Start=0
# Observed Time Series=Flow|TS Table Interval=1 Hour
# Observed Time Series=Flow|TS Table Data Units=cfs
# Observed Time Series=Flow|TS Table Data Type=INST-VAL
# Observed Time Series=Flow|TS Constant Units=cfs

ras_dss_file = '.\DSS_Input_Files\lwi_coastwide_usgs_refLines.dss'
with open(r'.\data\ObsDSS_ufile.txt', 'a+') as f:
    for BC_line in pathnamesnoDpart:
        bPart = BC_line.split('/')[2]
        f.write(f'Observed Time Series=Flow|TS Name=BC Line: {bPart}\n')
        f.write('Observed Time Series=Flow|TS Used=-1\n')
        f.write('Observed Time Series=Flow|TS Source=DSS\n')
        f.write(f'Observed Time Series=Flow|TS DSS Filename={ras_dss_file}\n')
        f.write(f'Observed Time Series=Flow|TS DSS Pathname={BC_line}\n')
        f.write('Observed Time Series=Flow|TS Table Mode=0\n')
        f.write('Observed Time Series=Flow|TS Table Use Fixed Start=0\n')
        f.write('Observed Time Series=Flow|TS Table Interval=1 Hour\n')
        f.write('Observed Time Series=Flow|TS Table Data Units=cfs\n')
        f.write('Observed Time Series=Flow|TS Table Data Type=INST-VAL\n')
        f.write('Observed Time Series=Flow|TS Constant Units=cfs\n')
# %%
