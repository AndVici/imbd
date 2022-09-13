from matplotlib import pyplot as plt
import numpy as np
import csv
import math
import sys
plt.style.use('ggplot')


def main():
#	A = ['0', '1']
#	B = [6102860, 44426]

	A = []
	B = []
	label = sys.argv[1]
	i=0
	with open(label +'.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		for row in reader:
			if(len(row)==0):
				continue
			if (i==0):
				A = list(row)
				i+=1
				continue
			if (i==1):
				B = list(row)
				i+=1
	
	A = A[1:]	
	B = B[1:]
	C = []
#	x = -1
	for i in range(len(B)):
		B[i] = int(B[i])
		#A[i] = int(A[i])

		if(A[i]=="imdbDisplay"):
			x = 10
		if(A[i]=="alternative"):
			x=20
		if(A[i]=="working"):
			x=30
		if(A[i]=="dvd"):
			x=40
		if(A[i]=="video"):
			x = 50
		if(A[i]=="tv"):
			x=60
		if(A[i]=="festival"):
			x=70
		if(A[i]=="original"):
			x=80
		
		C += [x]*B[i]
		
	print(len(C))
	print(B[0])
	
	plt.hist(C, bins = [10,20,30,40,50,60,70,80], align='left')
	
	labels = ["imdbDisplay","alternative","working","dvd","video","tv","festival","original"]
	
	

	plt.xticks([10,20,30,40,50,60,70,80], labels = labels, fontsize=7)
	plt.xlabel(label)
	plt.ylabel("number of movies")
	plt.title(label)
	plt.savefig(label+".png")
	plt.show()
	 
main()