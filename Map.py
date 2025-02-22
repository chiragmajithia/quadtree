import ReadShapeFile
import numpy as np
import matplotlib.pyplot as plt
from PolygonHandler import PolygonHandler
import os
import time
import scipy.misc

class Map(object):
	map
	polygons = PolygonHandler()
	imgplot = []

	def __init__(self,dim = [1,0],SCALE = 1,type = 'CSV'):
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


	def fillPoly(self,p):
		(x,y,r) = self.polygons.generateSeed(p)
		if r:
			self.fill(x,y)

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
				self.fill(x,y,fill_val = fill_val,bound_val = bound_val)
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

	def saveMap(self):
		np.savetxt(self.map,delimiter = ',')

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
			print 'does not exist'
			raw_input()
		else:
			self.imgplot.set_data(self.map)
			plt.draw()
			print 'exists'
			#time.sleep(0.01)
    # Figure is closed
		
		#plt.show(block = block)
		#plt.draw()
		#time.sleep(1)

	def getUnfilledPolygons(self):
		return self.polygons.unfilled_polygons