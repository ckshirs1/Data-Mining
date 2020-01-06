import csv

class AttributeStatistics:
	def __init__(self, attrNumber, attrName, min, max, mean, stDev):
		self.attrNumber = attrNumber
		self.attrName = attrName
		self.min = min
		self.max = max
		self.mean = mean
		self.stDev = stDev

attributeStatistics = []

with open('statisticsFile.txt') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for row in csv_reader:
		attributeStatistics.append(AttributeStatistics(int(row[0]), row[1], float(row[2]), float(row[3]),
		 float(row[4]), float(row[5])))

def getStatisticalData():
	return attributeStatistics