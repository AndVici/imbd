import csv
import os
import sys
import collections

csv.field_size_limit(sys.maxsize)

def main():
	label2 = "ratings"
	index2 = 14
	label = "runtimeMinutes"
	index = 7
	dict = {label : []}
	with open('21.table.2.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		for row in reader:
			if (len(row) == 0):
					continue
			if(row[index]!='\\N' and row[index2]!='\\N'):
				if row[index] in dict:
					dict[row[index]].append(row[index2])
				else:
					dict[int(row[index])] = [row[index2]]
	del dict[label]
	od = collections.OrderedDict(sorted(dict.items()))			
	
	with open("graphs/" +label+label2 +'2.tsv', 'w+', encoding='utf-8') as writefile:
		writer = csv.writer(writefile, delimiter='\t')
		x = len(dict)-1
		keyLi = [" "] * x
		valLi = [0] * x
		i=0
		for key, val in od.items():
			if(i==0):
				i+=1
				continue
			keyLi[i-1] = key
			valLi[i-1] = val
			i+=1
		writer.writerow(keyLi)
		writer.writerow(valLi)
	print(len(dict))
	
main()