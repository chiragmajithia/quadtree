import numpy as np 
import os
from PolygonHandler import PolygonHandler

def bfs():
	print 'in here..'

def fill(self, map, seed_x, seed_y):

    stack = set([(seed_x, seed_y)])
    ysize,xsize = map.shape
    while stack:
        x,y = stack.pop()

        if map[x, y] == 0:
            map[x, y] = 1
            if x > 0:
                stack.add((x - 1, ))
            if x < (xsize - 1):
                stack.add((x + 1, y))
            if y > 0:
                stack.add((x, y - 1))
            if y < (ysize - 1):
                stack.add((x, y + 1))


if __name__ == '__main__':
	bfs()
	path = os.path.dirname(os.path.abspath('resource'))
	path = os.path.join(path,'test.csv')
	polygons = PolygonHandler();
	polygons.readFile(path)
	polygons.correct()
	raw_input('correction done')
	polygons.disp()

'''
TODO : 
readFile():
confirm round numbers
First and Last vertex check -- closed loop polygons

REMEMBER:
polygons[p] -- p is the key, dont interchange it's use with index
'''