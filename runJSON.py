import Map
import matplotlib.pyplot as plt
from time import sleep

m = Map.Map(SCALE = 10,type = 'JSON')
#m.connectVertices()
m.fillAll() 
cnt = 1
# for p in m.polygons.polygons.keys():
# 	m.fillPoly(p)
# 	# if cnt%100 == 0:
# 	# 	plt.close("all")
# 	# 	m.showMap()
# 	# cnt += 1

#m.showMap()
m.saveImage(name = 'scale_2.jpg')