import pandas as pd

d1 = pd.read_csv('EGFR_activated_samples.txt', sep = "\t")

d2 = pd.read_csv('EGFR_mutations.txt', sep = "\t")

#create one single table
mergeDf = pd.merge(d1, d2, left_on = ['STUDY_ID', 'SAMPLE_ID'], right_on = ['STUDY_ID', 'SAMPLE_ID'])

#print(mergeDf)
mergeDf.to_csv(r'merged.txt', header=None, index=None, sep='\t', mode='a')