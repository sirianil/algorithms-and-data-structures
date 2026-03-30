from collections import defaultdict

class Solution:
    def find_anagrams(self, words):
        if len(words) == 0:
            return []
        
        anagrams = defaultdict(list)
        for word in words:
            sorted_word = str(sorted(word))
            anagrams[sorted_word].append(word)

        result = []
        for _, list_of_words in anagrams.items():
            result.append(list_of_words)
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.find_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(s.find_anagrams([""]))
    print(s.find_anagrams(["a"]))    