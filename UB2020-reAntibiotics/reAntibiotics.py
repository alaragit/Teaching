# Author: Adolfo Lara
# June 2020
# Exercise: Identify which medicine will be effective at treatement against a specific bacteria.
import re

#These are DNA segments that specific medicines cut. 
#Once the assigned piece of DNA is cut, it renders the DNA of that bacteria useless resulting in an effective treatment option. 

#Medicines:
MedA='ATTA'
MedB='TATA'
MedC='CCGG'
MedD='CTTA'

#Bacteria:
Bac1='GCTTCGATGGATGATTATTTCGATTGACTGAAACCTTGACTGAAGAATCC'
Bac2='TATAACGGAGCGACGCAGTGCGAGGGACGGAGCCGAGCGCTAGTGGTACA'
Bac3='AGGGCGGACCGCCCGGCCCCCGCGCCCCGTGCCTCGCCTGCGCTGGCGGG'
Bac4='TAAACCTTAATTTGCAGTCAGTCAATAGCGTAAATAACTTTGCAATGCGA'
Bac5='TCCCCCGACGGCCGTGCGGACCCGGGAGTGCGGGCACCCCCCGCGGGCCC'
Bac6='TACCACGAGGAGCACGAGTCATCCTAATACTGAATAATATTATTAGTGTC'
Bac7='TACGCTAGGTCACTCCATCCGAGGGACGCACTTACAGGAGGGCGCGCCGC'
Bac8='CCTCGGAGGCAGTGCACCGTAGCGCGCGGGCGGTATAGGGCCCTGCCCGT'
################################################################################################################################################################

################################################################################################################################################################
###Answer:

###List of bacteria
baclist = [Bac1,Bac2,Bac3,Bac4,Bac5,Bac6,Bac7,Bac8]


###Loops to test if a specific medicine can cut a section in the DNA of a given bacteria looping through all elements in the baclist.
###4 loops
for i in range(len(baclist)):
	if re.search(MedA,baclist[i]):
		print('Medicine',MedA,'works on bacteria',i+1)

###4 loops
for i in range(len(baclist)):
	if re.search(MedB,baclist[i]):
		print('Medicine',MedB,'works on bacteria',i+1)

###4 loops
for i in range(len(baclist)):
	if re.search(MedC,baclist[i]):
		print('Medicine',MedC,'works on bacteria',i+1)

###4 loops
for i in range(len(baclist)):
	if re.search(MedD,baclist[i]):
		print('Medicine',MedD,'works on bacteria',i+1)



