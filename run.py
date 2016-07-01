import ReadShapeFile
f = ReadShapeFile.FileGen()
f.openFile()
g = f.getGPS()
p = f.GPStoEUC()