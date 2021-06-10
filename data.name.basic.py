import sys
import os
import csv

csv.field_size_limit(sys.maxsize)

def main():	
	with open('data_3.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter ='\t')
	

		with open('name_basics_act.tsv', 'w+', encoding='utf-8') as writefile:
			writer = csv.writer(writefile, delimiter='\t')
			
			
			for row in reader:
				if(row[3].split(",")[0] == 'actor' or row[3].split(",")[0]=='actress'):
					writer.writerow(row)
				
main()