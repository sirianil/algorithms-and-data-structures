class WordDistance:

    def __init__(self, wordsDict: List[str]):
        words_map = defaultdict([])
        for i, word in enumerate(wordsDict):
            words_map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int: