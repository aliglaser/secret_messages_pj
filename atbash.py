from ciphers import Cipher

class AtbashCipher(Cipher):
	alphabetlist = list("abcdefghijklmnopqrstuvwxyz")
	rvsdalphabetlist = alphabetlist[::-1]

	def __init__(self):
		pass


	def printlist(self):
		print(self.rvsdalphabetlist)


	def encrypt(self, text=""):
		output=[]
		zipped = list(zip(self.alphabetlist, self.rvsdalphabetlist))
		for letter in text:
			for ori, rvsd in zipped:
				if ori == letter:
					output.append(rvsd)
		print("".join(output))	

	
	def decrypt(self, text=""):
		output =[]
		zipped = list(zip(self.alphabetlist, self.rvsdalphabetlist))
		for letter in text:
			for ori, rvsd in zipped:
				if rvsd == letter:
					output.append(ori)
		print("".ajoin(output))					
