from matplotlib import pyplot as plt
import numpy as np
import csv
import sys
plt.style.use('ggplot')

def main():

	A = []
	B = []
	label = sys.argv[1]
	i=0
	with open(label +'normalized.tsv', encoding='utf-8') as readfile:
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
	for i in range(len(B)):
		B[i] = int(B[i])

	print(len(A))
	print(len(B))
	
	fig = plt.figure()
	ax = fig.add_axes([0,0,1,1])

	x_pos = [i for i, _ in enumerate(A)]

	plt.bar(x_pos, B)
	plt.xlabel(label)
	plt.ylabel("number of movies")
	plt.title(label)
	plt.xticks(x_pos, A)
	
	plt.savefig(label+"normalized.png")
	plt.show()
	 
main()