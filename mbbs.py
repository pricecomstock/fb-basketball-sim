#facebook messenger basketball simulator
import sys
import random
import time

#probabilities of making a shot in each set of 10 baskets
#0-10, 11-20, 21-30, etc. in order
probs=[.8,0.9,0.5,0.3,0.15,0.1]

scores = []

def scoreReport():
	for x in range(max(scores)):
		print str(x) + " scored " + str(scores.count(x)) + " times!"
	print ""
	print "Attempts: " + str(len(scores))
	print "High score: " + str(max(scores))
	print "Average score: " + str(sum(scores)/float(len(scores)))

attempts = input("Please enter number of attempts: ")

while attempts > 0 :
	attempts -= 1
	madePrev=True
	made=0
	while(madePrev):
		if random.random() < probs[made / 10]:
			made += 1
			print "You have made " + str(made) + " shot(s)!"
		else:
			print "You missed a shot after making " + str(made) + " shots!"
			made=0
			madePrev=False
		time.sleep(1)
