import sys
import os
import csv

def main():	
	with open('data_1.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter ='\t')
	

		with open('data_movies.tsv', 'w+', encoding='utf-8') as writefile:
			writer = csv.writer(writefile, delimiter='\t')
			

			for row in reader:
				if(row[1] == 'movie'):
					writer.writerow(row)
				
main()