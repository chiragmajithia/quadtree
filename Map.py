import ReadShapeFile
import numpy as np
import matplotlib.pyplot as plt
from PolygonHandler import PolygonHandler
from eventHandler import MapEventHandler
import os
import time
import scipy.misc
from roipoly import roipoly

class Map(object):
	map
	polygons = PolygonHandler()
	imgplot = []
	event_flag = False
	event_cnt = 0
	meh = MapEventHandler() 
	r = None

	def __init__(self,dim = [1,0],SCALE = 1,type = 'CSV'):
		self.polygons = PolygonHandler()
		self.imgplot = []
		print 'In Map'
		path = os.path.dirname(os.path.abspath('resource'))
		if type == 'CSV':
			path = os.path.join(path,'Polygons1.csv')
		else :
			path = os.path.join(path,'pyshp.json')
		self.polygons.SCALE = SCALE
		self.polygons.readFile(path,type = type)
		self.polygons.correct()
		self.map = np.zeros(self.polygons.dim, dtype = np.uint8)
		self.event_flag = False
		self.event_cnt = 0
		self.meh = MapEventHandler()
		#raw_input('Vertices checked for closure - correction done')

	def connectVertices(self):

		for p,v in self.polygons.polygons.iteritems():
			indx = 0
			while indx < len(v) -1 :
				self.lineSeg(v[indx],v[indx+1])
				indx = indx + 1
		print "Vertices connected"

	def drawBoundary(self,key,fill_val = 255):
		v = self.polygons.polygons[key]
		#print v
		indx = 0
		while indx < len(v) -1 :
			self.lineSeg(v[indx],v[indx+1],fill_val = fill_val)
			indx = indx + 1
		print 'Vertices connected for polygon[' + str(key) + ']'

	def fillPoly(self,p,type = 'random'):
		self.drawBoundary(p,fill_val = 255)
		if type == 'random':
			(x,y,r) = self.polygons.generateRandomSeed(p)
		else:
			(x,y,r) = self.getSeed(p,255)
		if r:
			self.fill(x,y,fill_val = 255, bound_val = 255)

	def fillAll(self):
		bound_val = 100
		fill_val = 255

		for p in self.polygons.polygons:
			self.drawBoundary(p,fill_val = bound_val)
			#self.showMap()
			print('boundary drawn')
			(x,y,r) = self.getSeed(p,bound_val)
			fill_val = p%253 + 1
			print 'fill val = ' + str(fill_val)
			if r:
				print 'Filling polygon ' + str(p)
				self.fill(x,y,fill_val = fill_val,bound_val = bound_val)
				self.polygons.filled_polygons[p] = [x,y]
				#self.showMap()
			self.drawBoundary(p,fill_val = fill_val)
			if fill_val == 1:
				self.refreshMap()
		self.refreshMap()
		#self.showMap()

	def getSeed(self,p,bound_val):
		(x,y,r) = self.polygons.generateSeed(p)
		if r == False:
			self.polygons.unfilled_polygons[p] = [x,y,len(self.polygons.polygons[p]),'r']
		elif self.map[y,x] == bound_val:
			print 'on edge'
			(x_old,y_old) = (x,y)
			(x,y,r) = self.polygons.generateRandomSeed(p)
			if r == False:
				self.polygons.unfilled_polygons[p] = [x_old,y_old,len(self.polygons.polygons[p]),'e']
			#raw_input()
		return (x,y,r)

	def fillAllRandom(self):
		for p in self.polygons.polygons:
			(x,y,r) = self.polygons.generateRandomSeed(p)
			if r:
				self.fill(x,y)
		#self.showMap()

	def refreshMap(self):
		indices = self.map > 0
		self.map[indices] = 255
		print 'Map refreshed'
		#self.showMap()

	def fill(self,seed_x, seed_y, fill_val  = 255, bound_val = 255):
		stack = set([(seed_x, seed_y)])
		ysize,xsize = self.map.shape
		while stack:
			x,y = stack.pop()
			if not (self.map[y, x] == bound_val or self.map[y,x] == fill_val):
				self.map[y, x] = fill_val
				if x > 0:
					stack.add((x - 1,y))
				if x < (xsize - 1):
					stack.add((x + 1, y))
				if y > 0:
					stack.add((x, y - 1))
				if y < (ysize - 1):
					stack.add((x, y + 1))
				if x < (xsize - 1) and y < (ysize - 1):
					stack.add((x+1,y+1))
				if x < (xsize - 1) and y > 0:
					stack.add((x+1,y-1))
				if x > 0 and y < (ysize + 1):
					stack.add((x-1,y+1))
				if x > 0 and y > 0 : 
					stack.add((x-1,y-1))
					
			#print stack

			
	def lineSeg(self,v0,v1,fill_val = 255):
		x0 = v0[0]
		y0 = v0[1]

		x1 = v1[0]
		y1 = v1[1]
 		# Setup initial conditions
		dx = abs(x1 - x0)
		dy = abs(y1 - y0)
		x = x0
		y = y0
		n = 1 + dx + dy
		x_inc = 1 if x1 > x0 else -1
		y_inc = 1 if  y1 > y0  else -1
		error = dx - dy
		dx *= 2
		dy *= 2
		  # Traverse
		while n > 0:
		  self.map[x][y] = fill_val

		  if error >= 0:
		      x += x_inc
		      error -= dy
		  else:
		      y += y_inc
		      error += dx

		  n-=1

	def saveMap(self,name = 'map.csv'):
		np.savetxt(name,self.map,delimiter = ',',fmt = '%u')

	def saveImage(self, name = 'map.jpg'):
		self.map = np.invert(self.map)
		scipy.misc.imsave(name, self.map)
		self.map = np.invert(self.map)

	def showMap(self,block = False ):

		if not plt.fignum_exists(1):
			self.imgplot = plt.imshow(self.map,interpolation = 'none', cmap = 'gray_r')
			plt.show(block = block)
			plt.grid(1)
			plt.ion()
		else:
			self.imgplot.set_data(self.map)
			plt.draw()
			print 'exists'
			#time.sleep(0.01)

	def zoomPolygon(self,key,highlight = True):
		# self.refreshMap()
		if key == -1:
			self.resizeMap()
		else:
			(max_x,min_x,max_y,min_y) = self.polygons.getPolygonBounds(key)
			if highlight:
				self.drawBoundary(key,fill_val = 100)
				print 'draw'
				self.showMap()
			plt.axis([min_y-10,max_y+10,min_x-10,max_x+10])
		plt.draw()

	def zoomAllPolygons(self,event,check = True):
		self.showMap()
		print event.key
		k = self.event_cnt
		if event.key == ' ' or event.key == 'right':
			self.event_cnt += 1
			k = self.event_cnt
		elif event.key == 'left' or event.key == 'backspace':
			self.event_cnt -= 1
			k = self.event_cnt
		elif event.key == 'escape':
			self.event_cnt = -1
			self.zoomPolygon(-1)
			self.meh.disconnect()
			print 'returning to main menu'
			return
		if k >= 0 or k < len(self.polygons.polygons.keys()):
			self.zoomPolygon(self.polygons.polygons.keys()[k])

	def zoomFilledPolygons(self,event,check = True):
		self.showMap()
		print event.key
		k = self.event_cnt
		if event.key == ' ' or event.key == 'right':
			self.event_cnt += 1
			k = self.event_cnt
		elif event.key == 'left' or event.key == 'backspace':
			self.event_cnt -= 1
			k = self.event_cnt
		elif event.key == 'escape':
			self.event_cnt = -1
			self.zoomPolygon(-1)
			self.meh.disconnect()
			print 'returning to main menu'
			return
		if k >= 0 or k < len(self.polygons.filled_polygons.keys()):
			self.zoomPolygon(self.polygons.filled_polygons.keys()[k])


	def zoomUnfilledPolygons(self,event,check = True):
		self.showMap()
		print event.key
		k = self.event_cnt
		if event.key == ' ' or event.key == 'right':
			self.event_cnt += 1
			k = self.event_cnt
		elif event.key == 'left' or event.key == 'backspace':
			self.event_cnt -= 1
			k = self.event_cnt
		elif event.key == 'escape':
			self.event_cnt = -1
			self.zoomPolygon(-1)
			self.meh.disconnect()
			print 'returning to main menu'
			return
		if k >= 0 or k < len(self.polygons.unfilled_polygons.keys()):
			self.zoomPolygon(self.polygons.unfilled_polygons.keys()[k])

	def connectSeedingCallback(self):
		self.meh.connect()
		self.meh.eventClickConnect(self.eventFill)

	def connectKeyIteratorCallback(self,func):
		self.meh.connect()
		self.meh.eventKeyConnect(func)

	def nextIterator(self,event):
		print self.event_flag
		if event.key == 'N':
			self.event_flag = False
			print self.event_flag

	def eventFill(self,event):
		if event.inaxes:
			x, y = event.xdata, event.ydata
			ax = event.inaxes
			print 'Position = ' + str([x,y])
			print 'call back'
			k = self.polygons.pointInPoly(y,x)
			if k != -1:
				self.drawBoundary(k,fill_val = 255)
				self.fill(x,y,fill_val = 255, bound_val =255)
				# self.drawBoundary(k,fill_val = 255)
				self.showMap()
				print 'Filled'
			else:
				print 'point is outside any polygon'

	def resizeMap(self):
		self.refreshMap()
		if not plt.fignum_exists(1):
			self.imgplot = plt.imshow(self.map,interpolation = 'none', cmap = 'gray_r')
			plt.show(block = False)
			plt.grid(1)
			plt.ion()
		else:
			plt.axis([0,self.polygons.dim[1],self.polygons.dim[0],0])
			plt.draw()

	def addPolygon(self,vertices):
		k = len(self.polygons.polygons)
		self.polygons.polygons[k] = vertices
		self.fillPoly(k)
		self.showMap()

	def addPolygonsMenu(self):
		try:
			self.meh.disconnect() #surround try catch
		except BaseException:
			print "Error caught"
		self.displayAddPolygonMenu()
		self.showMap()
		self.r =roipoly(self.addPolygonCallback)

	def addPolygonCallback(self):
		inp = 1
		if inp == 1:
			v = self.r.getVertices()
			self.addPolygon(v)
			plt.close(1)
			self.showMap()
		# else:
		# 	print 'polygon discarded'
		# 	self.addPolygon(v)
		# 	plt.close(1)
		# 	self.showMap()


	def chooseViewMenu(self):
		self.displayViewMenu()
		inp = input('Enter a choice')
		print ('Press space/right arrow key to move forward')
		print ('Press left arrow key to move backward')
		print ('Press (ESC) to stop and Right Click to seed an empty polygon')
		if inp == 1:
			self.connectSeedingCallback()
			self.connectKeyIteratorCallback(self.zoomAllPolygons)
		elif inp == 2:
			self.connectSeedingCallback()
			self.connectKeyIteratorCallback(self.zoomFilledPolygons)
		elif inp == 3:
			self.connectSeedingCallback()
			self.connectKeyIteratorCallback(self.zoomUnfilledPolygons)
		elif inp == 4:
			print "Falling back to main menu"
		else:
			print "Illegal / Invalid input, falling back to main menu"

	def displayViewMenu(self):
		print "Enter your choice:: Do you want to Zoom"
		print "1.  all Polygons"
		print "2. Unfilled Polygons - the polygons for which the algorithm was not able to find seed to fill"
		print "                     - generally, these polygons are already filled with vertices defining its edges"
		print "3. Filled Polygons - the polygons which algorithm considers to be filled, but in cases where "
		print "                   - the edges of the polygons self intersect, the flood-fill algorithm is not able"
		print "                     fill the polygons completely"
		print "4 Fall back to main menu"

	def displayAddPolygonMenu(self):
		print "Add Polygon by drawing vertices on the figure, use left click to add vertices and right click to close polygon"
	