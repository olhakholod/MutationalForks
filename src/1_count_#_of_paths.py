fhand = open('BioGRID_Human_Interactome_EGFR_results.txt')

count = 0

for line in fhand:
	count = count + 1
print('Path count:', count)