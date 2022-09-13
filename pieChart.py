from matplotlib import pyplot as plt
import numpy as np
import csv
plt.style.use('ggplot')

def main():
#	A = ['0', '1']
#	B = [6102860, 44426]

	A = []
	B = []
	label = "language"

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

	for i in range(len(B)):
		B[i] = int(B[i])


	A = A[1:]

	B = B[1:]


	plt.pie(B, labels=A)
	plt.title=label
	plt.axis('equal')
	plt.savefig(label+".png")
	plt.show()
	 
main()