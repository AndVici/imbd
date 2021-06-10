import sys
import os
import csv
import copy

csv.field_size_limit(sys.maxsize)

def main():	
	readfile1 = open('name_basics_act.tsv', encoding='utf-8')
	
	act=readfile1.readline().split('\t')
	cc = ""
	temp = ""
	with open('data_us_movies.tsv', encoding='utf-8') as readfile2:
		reader2 = csv.reader(readfile2, delimiter='\t')	
		
		for mov in reader2:
			actors = []
			if(len(mov)==0):
				continue
			if(mov[0] =="tt0000009"):
				cc = mov[6]
			while(act[0]=='\n'):
				act=readfile1.readline().split('\t')
			while(act[0] < mov[0]):
				act=readfile1.readline().split('\t')
			while(mov[0]==act[0]):
				if(len(actors)==0):
					actors = act[2]
				else:
					actors = actors + "," + act[2]
				while(True):
					act=readfile1.readline().split('\t')
					if(act[0] != '\n'):
						break
			if(len(actors) == 0):
				mov.append(cc)
			else:
				mov.append(actors)
			with open('data_us_movies_actors1.tsv', 'a', encoding='utf-8') as writefile:
				csv.writer(writefile, delimiter='\t').writerow(mov)	
main()