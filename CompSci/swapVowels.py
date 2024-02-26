vowels = ['a', 'e', 'i', 'o', 'u']

def swapVowels(vowels, string):
	s_vowels = []
	for char in string:
		if char in vowels:
			s_vowels.append(char)
	vowelsLength = len(vowels)
	halfVL = vowelsLength // 2
	for num in range(0, halfVL):
		thisVowel = vowels[num]
		thatVowel = vowels[vowelsLength-num]
		string = string.replace(thisVowel, thatVowel)
