import shapefile
import shapely 
from matplotlib import pyplot
from descartes import PolygonPatch
from time import sleep
from shapely.geometry import Polygon
from shapely.geometry.polygon import LinearRing

BLUE = '#6699cc'
GRAY = '#999999'

#Load the shapefile of polygons and convert it to shapely polygon object

# read the shapefile

reader = shapefile.Reader("C:\Users\Brual\Desktop\Quadtree Creation and Path Planning\Naresh stuff\Brual\Files to Chirag\shape_files\landareas.shp")
fields = reader.fields[1:]
field_names = [field[0] for field in fields]
buffer = []
for sr in reader.shapeRecords():
	atr = dict(zip(field_names, sr.record))
	geom = sr.shape.__geo_interface__
	buffer.append(dict(type="Feature", \
	geometry=geom, properties=atr)) 

# write the GeoJSON file
from json import dumps
geojson = open("pyshp-demo.json", "w")
geojson.write(dumps({"type": "FeatureCollection",\
"features": buffer}, indent=2) + "\n")
geojson.close()