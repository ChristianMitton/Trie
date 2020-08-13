class Trie:
    def __init__(self):        
        self.dictionary = {}

    def addWord(self, word):
        ptr = self.dictionary
        for c in word:
            ptr[c] = {'*': False}
            ptr = ptr[c]
        
        ptr['*'] = True
    
    def contains(self, word):
        ptr = self.dictionary
        for c in word:
            if c in ptr:
                ptr = ptr[c]
            else:
                return False

        return True if ptr['*'] == True else False            
        
    
trie = Trie()

trie.addWord('luffy')
trie.addWord('nami')
trie.addWord('zoro')
trie.addWord('sanji')

print(trie.dictionary)

print(trie.contains('luffy'))
print(trie.contains('luff'))
print(trie.contains('luffyy'))

