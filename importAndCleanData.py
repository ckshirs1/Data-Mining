import csv
import statisticsOfData as stats

rowsOne, colsOne = (527,39)
arrOne = [[0 for i in range(colsOne)] for j in range(rowsOne)]
rows, cols = (527,38) 
arrTwo = [[0 for i in range(cols)] for j in range(rows)] 

fileSetOne = 'water-treatment.data'

statsOfData = stats.getStatisticalData()

def fillMissingValuesAndNormalizeData():
	i=0
	j=0
	with open(fileSetOne) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			for value in row:
				if(value == '?'):
					value = getMeanValOfThisAttr(j-1)
				if(j==0):
					arrOne[i][j] = value
					j = j + 1 
					continue
				arrOne[i][j]=float(value)
				arrTwo[i][j-1]=(arrOne[i][j]-statsOfData[j-1].min)/(statsOfData[j-1].max-statsOfData[j-1].min)
				j=j+1
			i=i+1
			j=0
	return arrTwo

def getMeanValOfThisAttr(j):
	return statsOfData[j].mean