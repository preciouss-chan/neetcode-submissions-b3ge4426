from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordCache = set(wordDict)

        @lru_cache(None)
        def canBreak(i):
            if i == len(s):
                return True
            
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordCache and canBreak(j):
                    return True
                
            return False
        
        return canBreak(0)