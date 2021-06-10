"""	author Imara Johnson
	param attribute normalization: (standard, minmax, 
		softmax, decimal, sigmoid, all)
	$python normalization.py [attribute] [type]
	appends results to the end of the file. if
	using all, its in this order: 
		sigmoid, decimal, standard, minmax, softmax
"""
import csv
import os
import sys
import math

#	{"attribute": [min value, max value, number of values, mean]}
dict = {"startYear" : [1894, 2028, 5923977, 2009],	
	"runtimeMinutes" : [1, 51420, 5631513, 98],
	"ratings" : [1, 10, 5361156, 6.3],
	"numVotes" : [5,2286225, 5361156, 2258],
	"birthYear" : [12, 2018,1472078, 1958]}



def minmax(label, value):
	return (value - dict[label][0])/(dict[label][1]-dict[label][0])

#	find standard deviation
#	string	attribute	
#	array	values
#	array	value instances
def dev(label, a, b):
	N = dict[label][2]
	mu = dict[label][3]
	sum = 0
	for i in range(len(a)):
		sum += (math.pow(float(a[i])-mu,2))*int(b[i])
	delta = math.sqrt(sum/N)
	return delta
	
#	str		attribute
#	float	value
#	float	standard deviation
def softmax(label, x, delta):
	a = (x-dict[label][3])/delta
	return 1/(1+math.pow(math.e, a*-1))

#	standard normalization
def standard(value):
	x= (1/math.sqrt(2*math.pi)) * math.pow(math.e, -1/2*math.pow(value,2))
	return x

#	find divisor for decimal normalization
def findDiv(label):
	i = 10
	while(dict[label][1]//i>0):
		i = i*10
	return i

def decimal(div, value):
	return value/div
	
def sigmoid(value):
	return 1/(1+math.pow(math.e,-1*value))
	
	
def main():

	A = []
	B = []
	label = sys.argv[1]
	type = sys.argv[2].lower()
	i=0
	with open("graphs/"+label +'.tsv', encoding='utf-8') as readfile:
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
	if label not in dict:
		sys.exit("invalid attribute")

		
	if(type == "decimal" or type=="standard" or type=="sigmoid"):
		div = findDiv(label)
		for i in range(len(B)):
			A[i] = decimal(div, float(A[i]))

	if(type=="standard"):
		for i in range(len(B)):

			A[i] = standard(A[i])
	elif(type=="minmax"):
		for i in range(len(B)):
#			B[i] = int(B[i])
			A[i] = minmax(label, float(A[i]))
	elif(type=="sigmoid"):
		for i in range(len(B)):
#			B[i] = int(B[i])
			A[i] = sigmoid(A[i])
	elif(type=="softmax"):
		delta = dev(label, A, B)
		for i in range(len(B)):
			A[i] = softmax(label, float(A[i]), delta)
	elif(type=="all"):
		C =[0]*len(A)
		D =[0]*len(A)
		E =[0]*len(A)
		F =[0]*len(A)
		delta = dev(label, A, B)
		for i in range(len(B)):
			div = findDiv(label)
			C[i]= decimal(div, float(A[i]))
			E[i]= minmax(label, float(A[i]))
			D[i]= standard(C[i])
			F[i]= softmax(label, float(A[i]),delta)
			A[i] = sigmoid(C[i])
	else:
		sys.exit("invalid normalization")
	
	
	with open('graphs/'+label +'.tsv', 'a+', encoding='utf-8') as writefile:
		writer = csv.writer(writefile, delimiter='\t')
		writer.writerow(A)
		if type=="all":
			writer.writerow(C)
			writer.writerow(D)
			writer.writerow(E)
			writer.writerow(F)


main()