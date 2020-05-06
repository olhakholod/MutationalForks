import pprint

counts = {}

with open('connected_nodes.txt', 'r') as filehandle:
    
    for i in filehandle:

        node = i.split('\t')[0].rstrip()
        
        if node not in counts:
            counts[node] = 1

        else:
            counts[node] += 1

for i in sorted (counts) : 
#    print ((i, counts[i]), end = " ") 
    pprint.pprint(counts, width = 1)

#print(counts)