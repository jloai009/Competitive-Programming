class Solution(object):
    def wordBreak(self, s, wordDict):
        TrieNode = lambda: defaultdict(TrieNode)
        Trie = TrieNode()
        
        for w in wordDict:
            p = Trie
            for c in w:
                p = p[c]
            p['\0'] = True
            
    
        return self.search(s, Trie, 0, set())
    
    def search(self, s, Trie, j, cache):
        
        p = Trie
        for i in range(j, len(s)):
            c = s[i]
            if '\0' in p:
                if (i, c) not in cache:
                    cache.add((i, c))
                    if self.search(s, Trie, i, cache):
                        return True
            if c in p:
                p = p[c]
            else:
                return False
            
        return '\0' in p
