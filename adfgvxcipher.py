from ciphers import Cipher
import numpy

class ADFGVXCCipher(Cipher):
	wordlist = [
		list('abcdef'),
		list('hijklm'),
		list('nopqrs'),
		list('tuvwx'),
		list('yz0123'),
		list('456789'),
	]
	e_index = list('ADFGVXC')		


	def encrypt(self, text):
		output=[]
		for row in self.wordlist:
			for item in row:
				for letter in text:	
					if item == letter:
						index1=self.wordlist.index(row)
						index2=row.index(item)
						output.append(self.e_index[index1]+self.e_index[index2])
						#print(row.index(item))
		return(output)
	

	def decrypt(self, text=""):
		output = []
		index1 = 0
		index2 = 0
		for letters in text:
			print(letters)
			for code in self.e_index:
				if letters[0] == code:
					index1 = self.e_index.index(code)
					print(index1)
				if letters[1] == code:
					index2 = self.e_index.index(code)
					print(index2)	
				output.append(self.wordlist[index1][index2])		
		print(output)			

