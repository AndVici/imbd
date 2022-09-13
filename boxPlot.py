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
	for i in range(len(B)):
		B[i] = int(B[i])

		A[i] = float(A[i])

		
		#if(len(C)==0):
		#	C = [A[i]]*B[i]
		#else:
		C += [A[i]]*B[i]
		
	r = plt.boxplot(C)
	top = r["fliers"][0].get_data()[1]
	with open('outliers.tsv', 'a+', encoding='utf-8') as writefile:
		writer = csv.writer(writefile, delimiter='\t')
		writer.writerow([label, len(top)])
	print(len(top))
	print(top)
#	bot = r["fliers"][2].get_data()[1]
#	print(bot)
	# outlier_dict={top[0]:0}
	# for x in top:
		# if x in outlier_dict:
			# outlier_dict[x] +=1
		# else:
			# outlier_dict[x] = 1
	# with open(label+'outliers' +'.tsv', 'w+', encoding='utf-8') as writefile:
		# writer = csv.writer(writefile, delimiter='\t')
		# x = len(outlier_dict)
		# keyLi = [0] * x
		# valLi = [0] * x
		# i=0
		# for key in outlier_dict:
			# keyLi[i] = key
			# valLi[i] = outlier_dict[key]
			# i+=1
		# writer.writerow(keyLi)
		# writer.writerow(valLi)
	

	# x_pos = [i for i, _ in enumerate(A)]
	# plt.plot(x_pos, B)
	# plt.xlabel(label)
	# plt.ylabel("number of movies")
	plt.title(label)
	# plt.xticks(x_pos, A)
	#plt.savefig(label+".png")
	plt.show()
	 
main()