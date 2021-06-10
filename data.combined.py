import sys
import os
import csv

csv.field_size_limit(sys.maxsize)

def main():	
	readfile1 = open('title.ratings.tsv', encoding='utf-8')
	
	rat=readfile1.readline().split('\t')
	cc = ""
	with open('data_us_movies_actors1.tsv', encoding='utf-8') as readfile2:
		reader2 = csv.reader(readfile2, delimiter='\t')	
		
		for mov in reader2:
			rating = cc
			if(len(mov)==0):
				continue
			if(mov[0] =="tt0000009"):
				cc = mov[6]
			if(len(rat)==0):
				rat=readfile1.readline().split('\t')
			while(rat[0] < mov[0]):
				rat=readfile1.readline().split('\t')
			if(mov[0]==rat[0]):
				rating = rat[1]
				rat=readfile1.readline().split('\t')
			mov.append(rating)
			with open('data_combined2.tsv', 'a', encoding='utf-8') as writefile:
				csv.writer(writefile, delimiter='\t').writerow(mov)	
main()