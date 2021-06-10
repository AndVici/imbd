import sys
import os
import csv

csv.field_size_limit(sys.maxsize)

def main():	
	readfile1 = open('data_US.tsv', encoding='utf-8')
	
	row2=readfile1.readline().split('\t')

	with open('data_movies.tsv', encoding='utf-8') as readfile2:
		reader2 = csv.reader(readfile2, delimiter='\t')
			
		for row in reader2:
			if(len(row)==0):
				continue
			if(len(row2)==0):
				row2=readfile1.readline().split('\t')
			while(row[0] > row2[0]):
				row2 = row2=next(readfile1).split('\t')
			if(row[0] < row2[0]):
				continue
			if(row[0]==row2[0]):
				with open('data_us_movies.tsv', 'a', encoding='utf-8') as writefile:
					csv.writer(writefile, delimiter='\t').writerow(row)
						
main()