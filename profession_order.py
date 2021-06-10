import csv
import os
import sys
import collections

csv.field_size_limit(sys.maxsize)

def main():
	dict ={"startYear": 4, "runtimeMinutes": 5, "ratings":10,"numVotes":11,"birthYear":14}
	label = sys.argv[1]
	index = dict[label]
	genre = {-1 : 0}
	with open('final.table.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		for row in reader:
			if (len(row) == 0):
					continue
			if(row[index]!='\\N' and row[index] != label):
				if int(row[index]) in genre:
					genre[int(row[index])] +=1
				else:
					genre[int(row[index])] = 1
	od = collections.OrderedDict(sorted(genre.items()))			
	
	with open('graphs/' +label +'.tsv', 'w+', encoding='utf-8') as writefile:
		writer = csv.writer(writefile, delimiter='\t')
		x = len(genre)
		keyLi = [" "] * x
		valLi = [0] * x
		i=0
		for key, value in od.items():
			if(i==0):
				i+=1
				continue
			keyLi[i] = key
			valLi[i] = genre[key]
			i+=1
		writer.writerow(keyLi)
		writer.writerow(valLi)
	print(len(genre))
	
main()