my_dict = input("Enter the dictionanry path : ")
if len(my_dict) == 0:
	my_dict = './dico-fr.txt' # Edit this line as you wish 
else:
	pass
word_to_search_anagram = input("Enter the word you like to search the anagram for : ")

def anagram_hunter():
	with open(my_dict,'r') as dictio:
		words = dictio.readlines()
	for word in words:
		word = word.strip("\n")

		if len(word) == len(word_to_search_anagram):
			state = True
			for lettre in word_to_search_anagram.lower():
				if lettre in word.lower():
					state = True
					continue
				else:
					state = False
					break
			if state is True:
				print(word)
			else:
				pass
		else:
			pass
anagram_hunter()
