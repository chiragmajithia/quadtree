import csv
import numpy as np 
import ReadShapeFile
from numpy import subtract
from random import randint
class PolygonHandler(object):
	SCALE = 100;
	polygons = {}
	seeds = {}
	origin = [0,0]
	dim = [0,0]
	unfilled_polygons = {}
	filled_polygons = {}

	def __init__(self):
		self.unfilled_polygons = {}
		self.filled_polygons = {}
		self.seeds = {}
		self.polygons = {}
		self.origin = [0,0]
		self.dim = [0,0]
		
	def disp(self):
		print 'origin' + str(self.origin)
		print 'dim' + str(self.dim)
		for p in self.polygons:
		    print 'indx ='+ str(p)+'first = ' + str(self.polygons[p][0]) + ' last = ' + str(self.polygons[p][len(self.polygons[p])-1]) + 'number of vertices :: ' + str(len(self.polygons[p]))
		    raw_input()


	def correct(self):
		del_list = list()
		for p in self.polygons:
			first = set(self.polygons[p][0])
			last = set(self.polygons[p][len(self.polygons[p])-1])
			if(first == last):
				#print str(p)+' passed with ' + str(len(self.polygons[p])) + 'vertices'
				continue
			else:
				print str(p)+' failed with ::  first = ' + str(first) + ' last =' + str(last) +' with ' + str(len(self.polygons[p])) + 'vertices'
				del_list.append(p)
				#raw_input()
		for p in del_list:
			del self.polygons[p]
		print 'Vertices checked for closed polygons..'


	def maxminXY(self):
		max_x,max_y = 0,0
		min_x,min_y = self.polygons[0][0]
		for p in self.polygons:
			for v in self.polygons[p]:
				if max_x < v[0]:
					max_x = v[0]
				if max_y < v[1]:
					max_y = v[1]
				if min_x > v[0]:
					min_x = v[0]
				if min_y > v[1]:
					min_y = v[1]
		self.dim =[max_x - min_x, max_y - min_y]
		self.origin = [min_x,min_y]
		print 'Dimension of Map := ' + str(self.dim)
		print 'Origin of the Map := ' + str(self.origin)
		return max_x,max_y,min_x,min_y

	def generateSeed(self,key):
		print 'generating seed for ' + str(key) + 'polygon of size' + str(len(self.polygons[key]))
		(x,y) = np.mean(self.polygons[key],0)
		x = int(round(x))
		y = int(round(y))
		r = self.inside_polygon(x,y,self.polygons[key])
		if r:
			print 'centroid used for ' + str(key) + ' ! = ' + str([x,y])
			return y,x,r
		else:
			return self.generateRandomSeed(key)

	def getPolygonBounds(self,key):
		polygon = self.polygons[key]
		max_x = 0
		max_y = 0
		min_x = self.origin[0] + self.dim[0]
		min_y = self.origin[1] + self.dim[1]
		for v in polygon:
			if max_x < v[0]:
				max_x = v[0]
			if max_y < v[1]:
				max_y = v[1]
			if min_x > v[0]:
				min_x = v[0]
			if min_y > v[1]:
				min_y = v[1]
		return max_x,min_x,max_y,min_y

	def generateRandomSeed(self,key):
		polygon = self.polygons[key]
		(max_x,min_x,max_y,min_y) = self.getPolygonBounds(key)
		print max_x
		print max_y
		print min_x
		print min_y
		r = False
		cnt  = 0
		x = min_x
		y = min_y
		while (not r) and (cnt < 10000) :
			if not((max_x - min_x > 1) and (max_y - min_y > 1)):
				break
			cnt = cnt + 1
			x = randint(min_x+1,max_x)
			y = randint(min_y+1,max_y)
			r = self.inside_polygon(x,y,polygon)
			
			#print str(x) + ',' + str(y) + ' checking for polygon[' + str(key) + '] = ' + str(self.inside_polygon(x,y,polygon))
			#if cnt > 999:
				#print str(x) + ',' + str(y) + 'is inside polygon[' + str(key) + '] = ' + str(r)
				#print str(key) + 'cnt overflowed' + str(cnt)
			#raw_input()
		print 'Final ' + str(x) + ',' + str(y) + 'is inside polygon[' + str(key) + '] = ' + str(r)		
		# if not r:
		# 	raw_input('Press Key to continue..')
		# 	self.unfilled_polygons[key] = [x,y]
		return y,x,r

	def pointInPoly(self,x,y):
		k = -1
		for p,polygon in self.polygons.iteritems():
			if self.inside_polygon(x,y,polygon):
				k = p
		return k

	def inside_polygon(self,x, y, points):
	    """
	    Return True if a coordinate (x, y) is inside a polygon defined by
	    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].

	    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
	    """
	    n = len(points)
	    inside = False
	    p1x, p1y = points[0]
	    for i in range(1, n + 1):
	        p2x, p2y = points[i % n]
	        if y > min(p1y, p2y):
	            if y <= max(p1y, p2y):
	                if x <= max(p1x, p2x):
	                    if p1y != p2y:
	                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
	                    if p1x == p2x or x <= xinters:
	                        inside = not inside
	        p1x, p1y = p2x, p2y
	    return inside

	def readFile(self,path,type = 'CSV'):
		if type == 'CSV':
			self.readCSV(path)
		elif type == 'JSON':
			self.readJSON(path)
		else:
			print 'invalid type'

	def readJSON(self,path):
		f = ReadShapeFile.FileGen()
		f.openFile()
		g = f.getGPS()
		self.polygons = f.GPStoEUC()
		self.maxminXY()
		self.updatePolygons()
		print 'Polygons and Map generated'
		return self.polygons

	def updatePolygons(self):
		self.origin[0] = int(round(self.origin[0]/self.SCALE))
		self.origin[1] = int(round(self.origin[1]/self.SCALE))
		self.dim[0] = int(round(self.dim[0]/self.SCALE)) + 20
		self.dim[1] = int(round(self.dim[1]/self.SCALE)) + 20
		print 'Updating the coordinates to origin(' + str(self.origin) + ') and scale  = ' + str(self.SCALE)

		for p,polygon in self.polygons.iteritems():
			vertices = []
			for v in polygon:
					x = round(float(v[0])/self.SCALE) - self.origin[0]
					y = round(float(v[1])/self.SCALE) - self.origin[1]
					vertices.append([x,y])
			self.polygons[p] = vertices
		print 'Shifting euclidean coordinates to given origin done!'



	def readCSV(self,path):
		f = open(path, 'rb') # opens the csv file
		try:
		    reader = csv.reader(f,delimiter=',')  # creates the reader selfect
		    r = 0;
		    c = 0;
		    f_l = f.readline()
		    x =[x.strip() for x in f_l.split(',')]
		    #print 'first line'+str(x)
		    self.origin[0] = int(round(int(x[0])/self.SCALE))
		    self.origin[1] = int(round(int(x[1])/self.SCALE))

		    self.dim[0] = int(round((int(x[2])/self.SCALE) - self.origin[1])) + 2
		    self.dim[1] = int(round((int(x[3])/self.SCALE) - self.origin[0])) + 2
		    print self.origin
		    print self.dim
		    raw_input('origin,dim')
		    for row in reader:   # iterates the rows of the file in orders
		        vertices = [];
		        n = len(row) 
		        c = 0;
		        while(c < len(row)):
		        	if row[c] is not '':
		        		#print 'x,y['+str(c)+'] = '+ row[c] + ',' + row[c+1]
		        		x = round(float(row[c])/self.SCALE) - self.origin[1]
		        		y = round(float(row[c+1])/self.SCALE) - self.origin[0]
		        		vertices.append([int(x),int(y)])
		        		c = c + 2
		        	else:
		        		break
		        self.polygons[r] = vertices
		        r = r + 1
		finally:
		   f.close()      # closing
		return self.polygons
