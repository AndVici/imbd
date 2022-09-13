from matplotlib import pyplot as plt
import numpy as np
import csv
import math
import sys
plt.style.use('ggplot')


def main():

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
	
#	A = A[1:]	
#	B = B[1:]
	C = []
#	x =0
	for i in range(len(B)):
		B[i] = int(B[i])
		A[i] = float(A[i])
		C += [A[i]]*B[i]

	
	plt.hist(C, align='left')
	
	
	plt.xlabel(label)
	plt.ylabel("number of movies")
	plt.title(label)
	plt.savefig(label+"normalized.png")
	plt.show()
	 
main()