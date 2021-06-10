import csv

def main():
	actors = {}
	
	with open('actor.names.tsv', encoding='utf-8') as readfile2:
		reader = csv.reader(readfile2, delimiter='\t')
		
		for row in reader:
			if(len(row)==0):
				continue
			actors[row[0]] = row[1]
			
	with open('data_combined1.tsv', encoding='utf-8') as readfile:
		reader = csv.reader(readfile, delimiter='\t')
		
		for row in reader:
			if(len(row)==0):
				continue
			if(row[7].split('m')[0] == "n"):
				print(actors[row[7]])
				row[7] = actors[row[7]]
				
			with open('us_movies_act_names.tsv', 'a', encoding = 'utf-8') as writefile:
				csv.writer(writefile, delimiter='\t').writerow(row)
			
				
				
			
main()