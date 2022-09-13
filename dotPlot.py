from matplotlib import pyplot as plt
import numpy as np
import csv
import sys
import re
plt.style.use('ggplot')
csv.field_size_limit(sys.maxsize)

def main():
#	A = ['0', '1']
#	B = [6102860, 44426]

	A = []
	B = []
	label1 = "ratings"
	label = "runtimeMinutes"
	i=0
	with open(label + label1+'2.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		for row in reader:
			if(len(row)==0):
				continue
			if (i==0):
				A = list(row)
				i+=1
				continue
			if (i==1):
				for j in row:
					B.append(j)
				i+=1
	C=[]
	line = 0
	ex1 = ""
	ex2 = ""
	for i in range(len(B)):
		C.append(re.findall('\[([^[\]]*)\]', B[i]))
		temp = re.split("[',]", C[i][0])
		new =[]
		for j in range(len(temp)):
			if(line==0):
				ex1 = temp[0]
				ex2 = temp[3]
				line+=1
			3if(temp[j]!=ex1 and temp[j]!=ex2 and temp[j]!=label1):
			if(temp[j].isdigit()):
				new.append(float(temp[j]))
		C[i]=new
	
	A = A[:len(A)]
	for i in range(len(A)):
		if(A[i].isdigit()):
			A[i] = int(A[i])

#	x_pos = [i for i, _ in enumerate(A)]
	for Ax, By in zip(A, C):
		plt.scatter([Ax]*len(By), By, s=1)
	plt.xlabel(label)
	plt.ylabel(label1)
	plt.title(label+label1)
#	plt.xticks(x_pos, A)
	plt.savefig(label+label1+".png")
	plt.show()
	 
main()