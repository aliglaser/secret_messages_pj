import os
from atbash import AtbashCipher
from adfgvxcipher import ADFGVXCCipher
from keycipher import KeywordCipher
from caesar import Caesar




#Show the users the cipher options
def introduction():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("This is the Secret Messages project for the Treehouse Techdegree.")
	print("")
	print("""These are the current available ciphers:

1. Atbash
2. Caesar
3. ADFGVX
4. Keyword
""")


#list of the index number of the cipher list
cipher_list = ['1', '2', '3', '4']



#get an input and initiate cm(cipher method from Atbash, Caesar, ADFGVX, Keyword)
def initiating(methd):	
	if methd == "1":
		cm = AtbashCipher()
	elif methd == "2":
		cm = Caesar()	
	elif methd == "3":
		cm = ADFGVXCCipher()
	elif methd == "4":
		kwrd = input("Whats' your keyword? >")
		cm = KeywordCipher(kwrd)
	return cm


def cipher():
	while True:
		introduction()
		cipher_method=input("Which cipher would you like to use? ")
		if cipher_method in cipher_list:
			text = input("That's an excellent cipher. What's the message? >")
		else:
			qs=input("It's not on the list. Do you want to choose again? (y/n)  >")
			if qs.lower() == "n":
				break
			else:
				cipher()		
		choice = (input("Are we going to encrypt or decrypt? > ")).lower()
		cm = initiating(cipher_method)
		while True:
			if choice.lower() == "encrypt":
				result = cm.encrypt(text)
				break
			elif choice.lower() == "decrypt":
				result = cm.decrypt(text)
				break
			else:
				choice = input("You didnt' type it right. Choose between Encrypt/decrypt  >")	
		print(result)
		tryagain=input("Encrypt/decrypt something else? Y/n  >")
		if tryagain.lower() == "n":
			break
		else:
			cipher()	
			
		

if __name__ == "__main__":
	cipher()
	


