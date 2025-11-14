class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                current.children[i]=TrieNode()
            current=current.children[i]
        current.end=True
    def search(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                return False
            current=current.children[i]
        return current.end
    def start_with(self,word):
        current=self.root
        for i in word:
            if i not in current.children:
                return False
            current=current.children[i]
        return True
    
    def autocomplete(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        words = []

        def dfs(node, path):
            if node.end:
                words.append("".join(path))  # fixed line here
            for char, child in node.children.items():
                dfs(child, path + [char])

        dfs(current, list(prefix))
        return words

x=Trie()
x.insert('hello')
x.insert('weather')
print(x.search('weather'))
print(x.autocomplete('hel'))