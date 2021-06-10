import csv
import os
import sys

csv.field_size_limit(sys.maxsize)

def main():
	with open('data_combined2.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		with open('data_combined1.tsv', 'w+', encoding='utf-8') as writefile:
			writer = csv.writer(writefile, delimiter='\t')
			for row in reader:
				if (len(row) == 0):
					continue
				temp = [row[0],row[2], row[3], row[4], row[5], row[6], row[7], "", row[10]]
				genres = row[8].split(",")
				for i in genres:
					temp[7]=i
					writer.writerow(temp)
				actors = row[9].split(",")
				if(actors[0] != "None"):	
					for i in actors:
						temp[7] = i
						writer.writerow(temp)

main()
				