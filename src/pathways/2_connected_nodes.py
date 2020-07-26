fhand = open('GNA11_PathwayCommons_directed.txt')

for line in fhand:
	line = line.rstrip()
	if not line.startswith('>GNA11'):
		continue

	words = line.split()
#	print(words[0])

	path = words[0]
	pieces = path.split('>')
	print(pieces[2])
