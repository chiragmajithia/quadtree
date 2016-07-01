import json
from Matlab import lla2ecef,ecef2ned
from numpy import array,dot
from math import pi,sqrt,sin,cos,tan,atan

class FileGen(object):
	file
	polygons = {}
	gps = {}
	min_long = 0
	min_lat = 0
	def openFile(self,file_path = 'resource/pyshp.json'):

		self.file = json.loads(open(file_path).read())
		print(file_path + 'File opened!')

	def printKeys(self,dic):
		for k in dic.keys():
			print k

	def getGPS(self):
		self.min_long = self.file['features'][0]['geometry']['coordinates'][0][0][0]
		self.min_lat = self.file['features'][0]['geometry']['coordinates'][0][0][1]

		indx = 0
		for polygons in self.file['features']:
			for polygon in polygons['geometry']['coordinates']:
				self.gps[indx] = polygon
		 		indx += 1
		 		min_long = min(polygon, key = lambda t: t[0])[0]
		 		min_lat = min(polygon, key = lambda t: t[1])[1]
		 		if self.min_long > min_long:
		 			self.min_long = min_long
		 		if self.min_lat > min_lat:
		 			self.min_lat = min_lat

		return self.gps

	#TODO:: Check implementation


	def GPStoEUC(self):
		ned_orig = array([self.min_lat * (pi/180), self.min_long * (pi/180)]).transpose()
		polys = {}
		for indx in self.gps:
			polygon = self.gps[indx]
			poly = list()
			#print 'polygon = ' + str(polygon)
			for matrix_coord in polygon:
				x_lla = array([matrix_coord[1] * (pi/180), matrix_coord[0] * (pi/180)]).transpose() # phi (rad); lambda (rad)
				x_ecef = lla2ecef(array([x_lla[0], x_lla[1], 0]).transpose())
				# print 'x_cef' + str(x_ecef)
				# raw_input()
				x_ned = ecef2ned(ned_orig, x_ecef)
				#print 'x_ned' + str(x_ned)
				# raw_input()
				poly.append([x_ned[0],x_ned[1]])
				#print matrix_coord
				#print x_ned
			polys[indx] = poly
		return polys