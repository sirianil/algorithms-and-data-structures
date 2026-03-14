"""
Time of Start: 7:20 PM
Time at start solutioning:
Time at start coding:
time at testing:
time at submission:
"""

"""
"leetcode" -> "leet, code"
"applepenapple" -> "apple", "pen"
first thought is - have a set that contains lengths of all words in the dict
that way i can compare

start with an index. compare it one word in the trie.
if the word matches, take the remaining word and compare to the trie again.
if it doesn't work, backtrack -> compare with other words in the trie.
leet "code"
apple pen apple -> 
catsandog -> "cats" "dog" "sand" "and" "cat"

1. cats - and - og
2. cats - andog
3. catsandog -> cat sandog -> cat sand og

recursion -> check if first part of string matches any word;
if it does -> check again for the remaining.
if you get empty string it means you can return True.
if you get True -> then return True overall
"""

class Solution:
    def word_break(self, s, words): # code len=4
        return self.word_break_dp(s, words, set())
    
    def word_break_dp(self, s, words):
        if len(s) == 0:
            return True
        
        for word in words: # code
            if word == s[:len(word)]:
                if self.word_break(s[len(word):], words):
                    return True
        return False
    
    def wordBreakDPReal(self, s, words):
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        print(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.wordBreakDPReal("leetcode", ["leet", "code"]))
