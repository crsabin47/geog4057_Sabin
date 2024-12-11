import arcpy
import os
import ee
import pandas as pd

"""
Example usage: 
Python Project2.py
"""
def getGeeelevation(workspace,csv_file,outfc_name,epsg=4326):

    """
    workspace directory that contains inputs and outputs.
    csv file: input csv  filename
    epsg: wkid code for the spatial reference , e.g. 4326
    """

    #Load the CSV file
    csv_file = os.path.join(workspace,csv_file)
    data = pd.read_csv(csv_file)
    dem = ee.Image("USGS/3DEP/10m")
    geometry = [ee.Geometry.Point([x,y], f'EPSG:{epsg}') for x,y in zip(data['X'],data['Y'])]
    fc = ee.FeatureCollection(geometry)
    origin_info = fc.getInfo()
    sampled_fc = dem.sampleRegions(
        collection=fc,
        scale=10,
        geometries=True
    )
    sampled_info = sampled_fc.getInfo()
    for index, item in enumerate(origin_info['features']):
        item['properties'] = sampled_info['features'][index]['properties']
    fcname = os.path.join(workspace,outfc_name)
    if arcpy.Exists(fcname):
        arcpy.management.Delete(fcname)
    arcpy.management.CreateFeatureclass(workspace,outfc_name,geometry_type='POINT',spatial_reference=epsg)
    arcpy.management.AddField(fcname, field_name='elevation',field_type='FLOAT')
    with arcpy.da.InsertCursor(fcname,['SHAPE','elevation']) as cursor:
        for feat in origin_info['features']:
            #get the coordinates and create a point geometry
            coords = feat['geometry']['coordinates']
            points = arcpy.PointGeometry(arcpy.Point(coords[0],coords[1]),spatial_reference=32119)
            #get the properties and write it to elevation
            elev = feat['properties']['elevation']
            cursor.insertRow([points,elev])
    
def main():
    import sys
    try:
        ee.Initialize()
    except:
        ee.Authenticate()
        ee.Initialize()
    workspace = sys.argv[1]
    csv_file = sys.argv[2]
    outfc_name = sys.argv[3]
    epsg = int(sys.argv[4])

    getGeeelevation(workspace=r'C:\Users\crsab\OneDrive\Documents\Programming\geog4057_Sabin\Project2',csv_file='boundary.csv',outfc_name='pnt_elev1',epsg=32119)


if __name__ == '__main__':
    main()


