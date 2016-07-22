import sys
import matplotlib.pyplot as plt
import matplotlib.path as mplPath

class MapEventHandler(object):

	fig = []
	ax = []
	roicolor = 'b'

	def __init__(self):
		self.roicolor = 'b'
		self.click_event = None
		self.key_event_id = None

	def connect(self,fig = [], ax = [], roicolor = 'b'):
		if fig == []:
			self.fig = plt.gcf()
			if self.fig == []:
				print 'The image does not exist'

		if ax == []:
			self.ax = plt.gca()
			if self.ax == []:
				print 'The axis does not exist'
		self.roicolor = roicolor
		self.close_event_id = self.fig.canvas.mpl_connect('close_event',self.disconnect)
		
	def eventKeyConnect(self,func):
		self.key_event_id = self.fig.canvas.mpl_connect('key_press_event',func)
		print 'key event connected'

	def eventClickConnect(self,func):
		self.click_event_id = self.fig.canvas.mpl_connect('button_press_event',func)
		print 'mouse click connected'

	def disconnect(self):
		self.fig.canvas.mpl_disconnect(self.key_event_id)
		self.fig.canvas.mpl_disconnect(self.click_event_id)
		print 'events disconnected'


	def callback(self,event):
		if event.inaxes:
			x, y = event.xdata, event.ydata
			ax = event.inaxes
			print 'Position = ' + str([x,y])
			print 'call back'
