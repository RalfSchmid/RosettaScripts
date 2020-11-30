##### parse ROSETTA score.sf file

### need regexes and command line args
import re
import sys


### set-up for parsing
if len(sys.argv) < 2 :
    scoresf = 'score.sf' # default
else:
    scoresf = sys.argv[1] # use argument instead

hits = {}   # dict needed for hits


### parse input file and populate hits dict, or die gracefully
try:
    with open(scoresf, 'r') as score:
        entries = score.readlines()     # list of lines
        for entry in entries:
            if re.match(r"^SCORE:\s+\d", entry):  # filter for relevant lines only
                line = re.split(r" {1,}", entry) #  line split by one or more spaces
                hits[line[55].rstrip()]=float(line[48]) # populate hits with entry interface_score pairs
                #print(hits)
except IOError:
    print("score.sf not accessible.\n Either put it in working directory, or give full path as command line argument.")


### output tsv file
out = open('rosetta_hits.tsv', 'w')
sorted_hits = sorted(hits.items(), key=lambda x: x[1], reverse=False) # go via tuple to use lambda function
for i in sorted_hits:
	out.write(i[0]+"\t"+str(i[1])+"\n")
out.close() 
        
