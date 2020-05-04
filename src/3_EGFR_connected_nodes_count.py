fhand = open('BioGRID_Human_Interactome_EGFR_results.txt')

words = list()

for line in fhand:
	line = line.rstrip()
	if not line.startswith('>EGFR'):
		continue

	words = line.split()
#	print(words[0])

	path = words[0]
	pieces = path.split('>')
#	print(pieces[2])
	conn_node = pieces[2]

counts = dict()

for node in conn_node:
    counts[node] = counts.get(node, 0) + 1 

maxval = None
maxkey = None
for key,val in counts.items() :
    if val > maxval:
        maxval = val
        maxkey = key   

print(maxkey, maxval)