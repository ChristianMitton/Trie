class Trie:
	def __init__(self):				
		children = {'*': False}
	
	def addWord(self, word):		
		for letter in word:
			children = self.children
			if letter in children:
				children = children[letter]
			else:
				children[letter] = {'*' = False}
				children = children[letter]
		children['*'] = True

	def contains(self, word):
        children = self.children        
        for l in range(len(word)):
            letter = word[l]

            if letter in children:                
                children = children[letter]
            else:
                return False   

            if l == len(word)-1:
				return True if children['*'] == True else False                

trie = Trie()


trie.addWord('words')
trie.addWord('wapol')
trie.addWord('boat')

print(trie.children)

print(trie.contains('boat'))


# If you just used the 'in' method with arrays instead of using a trie, 
# lookup would be o(n*k) where n is the length of the array, and k the lenghth of the longest string.
# If you used a trie, lookup would be o(k) where k is the length of the longest string








	