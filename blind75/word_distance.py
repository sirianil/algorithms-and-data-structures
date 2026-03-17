from collections import defaultdict

class WordDistance:
    def __init__(self, wordsDict):
        self.words_map = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.words_map[word].append(i)
        print(self.words_map)

    def shortest(self, word1: str, word2: str) -> int:
        word1Idx = self.words_map[word1]
        word2Idx = self.words_map[word2]

        min_1 = min(word1Idx)
        max_1 = max(word1Idx)
        
        min_2 = min(word2Idx)
        max_2 = max(word2Idx)
        # print("1", min_1, " ", max_1)
        # print("2", min_2, " ", max_2)

        diff1 = abs(max_1-min_2)
        diff2 = abs(max_2-min_1)
        
        return min(diff1, diff2)

if __name__ == '__main__':
    s = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
    print(s.shortest("makes", "coding"))