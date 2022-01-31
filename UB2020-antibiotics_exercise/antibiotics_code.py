#Author Adolfo Lara June 25 2020

import random
# Exercise: You are infected with bacteria characterized as: 13 blue, 6 red, and 1 white.
#In this infection, white bacteria is the hardest to kill.
bluebac=13
redbac=6
whitebac=1

#As part of the treatment, we will mimic medicine with dice. This list represents a dice roll 1-6.
#1,3,5,6 - you took medicine: remove 3 bacteria (blue first).
#2 or 4 - you forgot medicine: remove 0 bacteria, add 1 of each.
t = [1, 2, 3, 4, 5, 6]

#Antibiotics you take are for 10 days, thus variable "i" keeps track of them.
i = 0

#If you roll a "1, 3, 5, 6" this means you took your antibiotics.
#If you took your antibiotics, 3 bacteria die and none reproduce.
#The loop below will take away 3 bacteria at a time, starting with the blue then red and finally white bacteria.

#If you roll a "2, 4" this means you did not take your antibiotics.
#If you did not take your antibiotics, the bacteria will reproduce.
#The loop below will add 1 to each of the blue, red, and white, bacteria.

#At the end of 10 tries (days) if you have more than 5 white bacteria, bacteria win. 
while i < 10:
	s = random.choice(t)
	if bluebac > 0 and s==1:
		bluebac = bluebac - 3
	if bluebac > 0 and s==3:
		bluebac = bluebac - 3
	if bluebac > 0 and s==5:
		bluebac = bluebac - 3
	if bluebac > 0 and s==6:
		bluebac = bluebac - 3
	
	if bluebac <= 0 and redbac > 0 and s==1:
		redbac = redbac - 3
	if bluebac <= 0 and redbac > 0 and s==3:
		redbac = redbac - 3
	if bluebac <= 0 and redbac > 0 and s==5:
		redbac = redbac - 3
	if bluebac <= 0 and redbac > 0 and s==6:
		redbac = redbac - 3
	
	if bluebac <= 0 and redbac <= 0 and whitebac > 0 and s==1:
		whitebac = whitebac - 3
	if bluebac <= 0 and redbac <= 0 and whitebac > 0 and s==3:
		whitebac = whitebac - 3
	if bluebac <= 0 and redbac <= 0 and whitebac > 0 and s==5:
		whitebac = whitebac - 3
	if bluebac <= 0 and redbac <= 0 and whitebac > 0 and s==6:
		whitebac = whitebac - 3
	
	if s==2:
		bluebac = bluebac + 1
		redbac = redbac + 1
		whitebac = whitebac + 1
	if s==4:
		bluebac = bluebac + 1
		redbac = redbac + 1
		whitebac = whitebac + 1
	print('Your dice-roll number',i+1,'is',s)
	print(bluebac,redbac,whitebac)
	i = i + 1

if whitebac >= 5:
	print('Your distribution of bacteria after 10 days are:',bluebac,'blue',redbac,'red',whitebac, 'white,', 'this means you are dead.')
elif whitebac < 5:
	print('Your distribution of bacteria after 10 days are:',bluebac,'blue',redbac,'red',whitebac, 'white,', 'this means you are alive.')
