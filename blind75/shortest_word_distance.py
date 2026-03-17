class Solution:
    '''
    wordsDict = [practise, makes, perfect, coding, makes]
    word1=coding
    word2=practise
    '''
    def shortest_word_distance(self, wordsDict, word1, word2):
        global_min = float('inf')
        prevWord1 = prevWord2 = None

        for i in range(len(wordsDict)): #i=0
            if wordsDict[i] == word1:
                if prevWord2 != None:
                    global_min = min(global_min, (i-prevWord2))
                prevWord1 = i
            elif wordsDict[i] == word2:
                if prevWord1 != None:
                    global_min = min(global_min, (i-prevWord1))
                prevWord2 = i   #0
        return global_min

if __name__ == '__main__':
    s = Solution()
    print(s.shortest_word_distance(["practise", "makes", "perfect", "coding", "makes"], "makes", "coding"))
    print(s.shortest_word_distance(["a", "b"], "a", "b"))
