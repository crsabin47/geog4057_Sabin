import arcpy
import os
walk = arcpy.da.Walk(r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7",datatype="RasterDataset")
for dirpath, dirnames, filenames in walk:
    for file in filenames:
        print(os.path.join(dirpath, file))

import arcpy
from arcpy import env
env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
raster1 = "tm.img"
raster2 = "landcover.tif"
raster3 = "elevation"
desc1 = arcpy.da.Describe(raster1)
desc2 = arcpy.da.Describe(raster2)
desc3 = arcpy.da.Describe(raster3)
print(desc1["bandCount"])
print(desc2["bandCount"])
print(desc3["bandCount"])


import arcpy
from arcpy import env
env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
raster1 = "tm.img"
raster2 = "landcover.tif"
raster3 = "elevation"
R1bit = arcpy.management.GetRasterProperties("tm.img", "VALUETYPE")
r1BIT = R1bit.getOutput(0)
print(r1BIT)
R2bit = arcpy.management.GetRasterProperties("landcover.tif", "VALUETYPE")
r2BIT = R2bit.getOutput(0)
print(r2BIT)
R3bit = arcpy.management.GetRasterProperties("elevation", "VALUETYPE")
r3BIT = R3bit.getOutput(0)

import arcpy
from arcpy import env
env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
raster1 = "tm.img"
raster2 = "landcover.tif"
raster3 = "elevation"
R1X = arcpy.management.GetRasterProperties("tm.img", "CELLSIZEX")
r1X = R1X.getOutput(0)
print(r1X)
R1Y = arcpy.management.GetRasterProperties("tm.img", "CELLSIZEY")
r1Y = R1Y.getOutput(0)
print(r1Y)
R2X = arcpy.management.GetRasterProperties("landcover.tif", "CELLSIZEX")
r2X = R2X.getOutput(0)
print(r2X)
R2Y = arcpy.management.GetRasterProperties("landcover.tif", "CELLSIZEY")
r2Y = R2Y.getOutput(0)
print(r2Y)
R3X = arcpy.management.GetRasterProperties("elevation", "CELLSIZEX")
r3X = R3X.getOutput(0)
print(r3X)
R3Y = arcpy.management.GetRasterProperties("elevation", "CELLSIZEY")
r3Y = R3Y.getOutput(0)
print(r3Y)

import arcpy
from arcpy import env

env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"

raster1 = "tm.img"
raster2 = "landcover.tif"
raster3 = "elevation"

desc1 = arcpy.Describe(raster1)
spatial_ref1 = desc.spatialReference
desc2 = arcpy.Describe(raster2)
spatial_ref2 = desc.spatialReference
desc3 = arcpy.Describe(raster3)
spatial_ref3 = desc.spatialReference
# Print the spatial reference
print(spatial_ref1.name)
print(spatial_ref2.name)
print(spatial_ref3.name)


import arcpy
from arcpy.sa import *
elev = arcpy.Raster("elevation")
outraster = Slope(elev)
outraster

Render (elev, colormap="Elevation #1")

from arcpy.sa import *
from arcpy.ia import *
elev_clip = Clip(elev, "watershed_HUC12.shp")

elev_clip.save("elev_clip")
elev_clip

import arcpy
arcpy.env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
landsat = "tm.img"
desc = arcpy.da.Describe(landsat)
for rband in desc["children"]:
    name = rband["name"]
    ras = arcpy.Raster("tm.img" + "/" + name)
    print(ras.catalogPath)
    outreclass.save("lu_reclass")

#(band 3 - band 1) / (band 3 + band 1)

import arcpy
arcpy.env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
from arcpy.sa import *
tm_inras = arcpy.Raster("tm.img")
tm_outras = (tm_inras[2] - tm_inras[0]) / (tm_inras[2] + tm_inras[0])
tm_outras.save("tm_outras")

```python
import numpy as np
import arcpy
arcpy.env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
from arcpy.sa import Raster, RasterCellIterator
# read the elevation model
dem = Raster("elevation")
arcpy.env.overwriteOutput = True

#get knowledge about the input raster
raster_info = dem.getRasterInfo()
cell_x = dem.meanCellWidth
cell_y = dem.meanCellHeight

# change the raster info so the output type is 32bit unsigned integer
raster_info.setPixelType("U32")
#create a new raster based on the raster info
elev_relcass = Raster(raster_info)
#update the raster using cell iterator
with RasterCellIterator({'rasters':[dem,elev_reclas]}) as rci:
    for r, c in rci:
    if dem > 2000:
        new_value = 1
    else:
        new_value = 0
slopecon.save()
        # modify this block here to do the classification of elevation to 1 or 0

elev_relcass.save('elev_relcass')
```

import numpy as np
import arcpy
from arcpy.sa import Raster, RasterCellIterator
# read the elevation model
dem = Raster("elevation")
arcpy.env.overwriteOutput = True

#get knowledge about the input raster
raster_info = dem.getRasterInfo()
cell_x = dem.meanCellWidth
cell_y = dem.meanCellHeight

raster_info.setPixelType("U32")

elev_relcass = Raster(raster_info)

arcpy.env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
with RasterCellIterator({'rasters':[dem,elev_reclas]}) as rci:
    for row, col, values in rci:
        elevation = values[0]  # Access the elevation value from the first raster (dem)
        if elevation > 2000:
            new_value = 1
        else:
            new_value = 0
        values[1] = new_value

import arcpy
import numpy
arcpy.env.workspace = r"C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Assignment7\Ex7"
elev_raster = "elevation"
array = arcpy.RasterToNumPyArray(elev_raster)
print(array.min())
print(array.max())
print(array.mean())
print(array.std())


