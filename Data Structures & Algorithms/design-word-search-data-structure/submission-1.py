class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children={}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr=curr.children[c]
            else:
                curr.children[c]=self.TrieNode()
                curr=curr.children[c]
        curr.is_end=True
    
    def search(self, word: str) -> bool:
        def dfs(root,idx):
            cur = root 
            for i in range(idx,len(word)):
                if word[i] == '.':
                    for child in cur.children.values():
                        result = dfs(child,i+1)
                        if result:
                            return True
                    return False
                elif word[i] in cur.children:
                    cur=cur.children[word[i]]
                else:
                    return False
            return cur.is_end
        return dfs(self.root,0)
        


        
        
