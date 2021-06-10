import sys
import os
import csv

csv.field_size_limit(sys.maxsize)

def main():	
	with open('data.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter ='\t')
	

		with open('data_US.tsv', 'w+', encoding='utf-8') as writefile:
			writer = csv.writer(writefile, delimiter='\t')
			
			
			for row in reader:
				if(row[3] == 'US'):
					writer.writerow(row)
				
main()