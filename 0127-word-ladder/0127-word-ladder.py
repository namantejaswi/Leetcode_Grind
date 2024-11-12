class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        if endWord not in wordList: return 0
        
        
        wordList = set(wordList)
        
        q = deque([[beginWord,1]])        #word, level we at
        
        visited = set(beginWord)
        
        alpha = set('abcdefghijklmnopqrstuvwxyz')

        
        while q:
            
            node = q.popleft()
            current_word, level = node[0], node[1]
            
            for i in range(len(current_word)):
                
                for c in alpha:
                    
                    t_word = current_word[:i] + c + current_word[i+1:]
                    
                    if t_word == endWord:     return level + 1
                    
                    if t_word in wordList and t_word not in visited:
                        q.append([t_word,level+1])
                        visited.add(t_word)
                
                
        return 0