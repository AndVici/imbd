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
#	x =0
	for i in range(len(B)):
		B[i] = int(B[i])
		#A[i] = int(A[i])

		if(A[i]=="en"):
			x = 10
		if(A[i]=="es"):
			x=20
		if(A[i]=="yi"):
			x=30
		if(A[i]=="hi"):
			x=40
		C += [x]*B[i]
		
#	print(C[B[2]:])
	print(A[0])
	print(C[0])
	
	plt.hist(C, bins = [10,20,30,40], align='left')
	
	labels = ["en", "es", "yi", "hi"]
	
	

	plt.xticks([10,20,30,40], labels = labels)
	plt.xlabel(label)
	plt.ylabel("number of movies")
	plt.title(label)
	plt.savefig(label+".png")
	plt.show()
	 
main()