fhand = open('BioGRID_Human_Interactome_ALK_results.txt')

for line in fhand:
	line = line.rstrip()
	if not line.startswith('>ALK'):
		continue

	words = line.split()
#	print(words[0])

	path = words[0]
	pieces = path.split('>')
	print(pieces[2])