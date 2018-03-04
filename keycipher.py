from ciphers import Cipher

class KeywordCipher(Cipher):
	keywordList=[]
	alphabet="abcdefghijklmnopqrstuvwxyz"
	new_rule=[]
	final = []

	def __init__(self, keyword=""):
		for letter in keyword:
			if letter not in self.keywordList:
				self.keywordList.append(letter)

		rest_letters=(set(self.alphabet).difference(set(self.keywordList)))
		lrest=list(rest_letters)
		lrest.sort()
		self.new_rule.extend(self.keywordList)
		self.new_rule.extend(lrest)


	def encrypt(self, text=""):
		zipped = zip(self.alphabet, self.new_rule)
		zipped = list(zipped)
		for letter in text:
			for oril, newl in zipped:
				if letter == oril:
					self.final.append(newl)
		print("".join(self.final))	
	

"""
	def decrypt(self, text=""):
		zipped = zip(self.alphabet, self.new_rule)
		zipped = list(zipped)	
"""					
