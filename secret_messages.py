import os




def introduction():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("This is the Secret Messages project for the Treehouse Techdegree.")
	print("")
	print("""These are the current available ciphers:
-Alberti cipher
-Atbash cipher
-Caeser cipher #이미 있음
-Polybius square cipher
-Transposition cipher
-ADFGVX cipher
-Keyword ciphers #완성함
""")
	#input("Which cipher would you like to use? ")




def make_ciphr(keyword):
	keywordList=[]
	for letter in keyword:
		if letter not in keywordList:
			keywordList.append(letter)
	alphabet="abcdefghijklmnopqrstuvwxyz"
	print(len(alphabet))
	rest_letters=(set(alphabet).difference(set(keywordList)))
	lrest=list(rest_letters)
	lrest.sort()
	new_rule=[]
	new_rule.extend(keywordList)
	new_rule.extend(lrest)
	print(len(new_rule))
	print(new_rule)




if __name__ == "__main__":
	introduction()

