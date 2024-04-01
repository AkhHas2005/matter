#Tool to search for leetcode solutions 
solutionMapping = {2784: "isGood",
		   2444: "countSubarrays",
		   992: "subarraysWithKDistinct",
		   101: "isSymmetric"}

solutionsFile = open("leetcodeSolutions.py")
solutionsBank = solutionsFile.readlines()

solutionNum = int(input("Enter the number of the problem you want to find the solution of: "))
solution = ""
solutionFound = False

if solutionNum in solutionMapping.keys():
	solutionName = "def "+solutionMapping[solutionNum]
	for line in solutionsBank:
		if solutionName in line:
			solutionFound = True
		if solutionFound:
			while "return" not in line:
				solution += line
	print("\nThe solution is as follows:\n")
	print(solution)
else:
	print("\nThe solution could not be found")


