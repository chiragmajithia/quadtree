import Map
import matplotlib.pyplot as plt
from time import sleep, time
import numpy as np
import os
import csv

path = os.path.dirname(os.path.abspath('resource'))

start = time()
scale = 1000
m = Map.Map(SCALE = scale,type = 'JSON')
#m.connectVertices()
m.fillAll() 
cnt = 1
# for p in m.polygons.polygons.keys():
# 	m.fillPoly(p)
# 	# if cnt%100 == 0:
# 	# 	plt.close("all")
# 	# 	m.showMap()
# 	# cnt += 1

end= time()
print 'process time ::' + str((end - start))
#m.showMap()
print 'saving..'
m.saveImage(name = path + '/output_jpg/scale_'+str(scale)+'.jpg')
indices = m.map > 0
m.map[indices] = 1
m.saveMap(name = path + '/output_csv/scale_'+str(scale)+'.csv')

with open(path + '/output_log/scale_'+str(scale)+'.csv', 'w') as f:
	f.truncate()
	w = csv.writer(f)
	w.writerow(['total polygons',len(m.polygons.unfilled_polygons)])
	for p,v in m.polygons.unfilled_polygons.iteritems():
		w.writerow([p,v])
	w.writerow(['process time',(end-start)])
end= time()
print 'total time ::' + str((end - start))