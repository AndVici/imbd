from matplotlib import pyplot as plt
import numpy as np
import csv
import sys
plt.style.use('ggplot')

def sort(a):
	b=[0]*len(a)
	for i in range(1,len(a)):
		
		j = i
		while j >0:
			if a[j] < a[j-1]:
				t = a[j]
				a[j] = a[j-1]
				a[j-1] = t
				j = j-1
			else:
				break
	for i in range(len(a)):
		b[i] = a[i]
	return b
		

def median_smooth(a, window):
	b=[0]*len(a)
	i = 0
	for j in range(window,len(a)):
		b[i] = sort(a[i:j])[2]
		i +=1
	for j in range(1,window+1):
		b[len(a)-j] = b[i-1]
	return b
	

def main():
#	A = ['0', '1']
#	B = [6102860, 44426]

	A = []
	B = []
	C = []
	label = sys.argv[1]
	line = int(sys.argv[2])
	type = sys.argv[3]
	i=0
	with open(label +'.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		for row in reader:
			if(len(row)==0):
				continue
			if (i==0):
				A = list(row)
				
			elif (i==1):
				B = list(row)
			elif (i==line):
				C = list(row)
				break
			i+=1
			
			
	B = B[1:]
	A = A[1:]
	for i in range(len(B)):
		B[i] = int(B[i])
		A[i] = float(A[i])
		C[i] = float(C[i])
	

#	c = median_smooth(A, 5)

	x_pos = [i for i, _ in enumerate(A)]
	

	plt.plot(C, B)
	plt.xlabel(label)
	plt.ylabel("number of movies")
	plt.title(label)
#	plt.xticks(x_pos, A)
	plt.savefig(label+type+".png")
	plt.show()
	 
main()