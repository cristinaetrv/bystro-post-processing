import sys
import math

# open arg 1 for reading
f1 = open(sys.argv[1],'r') #this is the variant list from Bystro
f = open(sys.argv[2],'r') #this is the list of Caco1 IDs for case
f0 = open(sys.argv[3],'r') #this is the list of Caco0 IDs for controls
out = open(sys.argv[4],'w')

list1=[] #initializes my empty list should be Caco=1
for line in f: #iterate through each line in file
	li = line.split() #split the single line into a list on whitespace
	list1.append(li[0]) #adds the first column of each line to my list
list2=[] #initializes my empty list should be Caco=0
for line in f0: #iterate through each line in file
	li0 = line.split() #split the single line into a list on whitespace
	list2.append(li0[0]) #adds the first column of each line to my list	

for line in f1: #iterate through each line in file
	li = line.split() #split the single line into a list on whitespace
	hets = li[3].split(';')
	homs = li[4].split(';')
	hetcases = 0 
	hetcntls = 0
	homcases = 0
	homcntls = 0
	#for x,y in zip(hets,homs):
	for x in hets:
		if x in list1:
			hetcases += 1
		elif x in list2:	
			hetcntls += 1
	for y in homs:
		if y in list1:	
			homcases += 1
		elif y in list2:
			homcntls += 1
		#else:
		#	continue #just keep going through the for loop and skip the rest below here
	out.write(li[0]+'\t'+li[1]+'\t'+li[2]+'\t'+li[3]+'\t'+str(hetcases)+'\t'+str(hetcntls)+'\t'+str(homcases)+'\t'+str(homcntls)+'\t'+li[4]+'\t'+li[5]+'\t'+li[6]+'\t'+li[7]+'\t'+li[8]+'\t'+li[9]+'\t'+li[10]+'\t'+li[11]+'\t'+li[12]+'\n')
	#print homcntls

out.close()

#Example: python getHetHomNumFromBystro.py KRR1snpsMAF05only.txt FxpoiCases.txt FxpoiCntlswoSeiz.txt KRR1snpsMAF05whethomcounts.txt