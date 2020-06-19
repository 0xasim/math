#!/usr/bin/python3
import random, math

"""
https://qr.ae/pNKHoP
"""

def make_flips(no_of_flips):
	heads = tails = 0

	for flip in range(no_of_flips):
		result = random.randint(0,1)
		if result == 0 : heads+=1
		else : tails+=1

	discrepancy = abs(heads-tails)
	expected_discrepancy = math.sqrt((2*no_of_flips)/math.pi)
	result = {
		"heads":heads,
		"tails":tails,
		"discrepancy":discrepancy,
		"expected_discrepancy":expected_discrepancy
		}
	return(result)

def main():
	discrepancy = []
	eD = 0	#expected discrepancy
	no_of_flips = int(input("\nEnter no. of flips to make (in a single iteration). \n>"))
	iterations = int(input("\nEnter no. of iterations to make (discrepancy will be averaged out of multiple iterations).\n> "))

	for i in range(iterations):
		r = make_flips(no_of_flips)
		discrepancy.append(r["discrepancy"])
		eD = r["expected_discrepancy"]
		print("\nIteration: "+str(i)+"\nHeads: "+str(r["heads"])+"\nTAILS: "+str(r["tails"]))
		print("discrepancy: "+str(r["discrepancy"]))

	avg_discrepancy = sum(discrepancy)/len(discrepancy)
	print("\nAverage discrepancy found: "+str(avg_discrepancy))
	print("expected discrepancy: "+ str(eD))

if __name__ == "__main__":
	main()
