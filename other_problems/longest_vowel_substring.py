class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        p1 = p2 = cur_len = max_len = 0

        while p1 < len(s):
            if self.isVowel(s[p1]):
                p2 = p1 + 1
                cur_len = 1
                while p2 < len(s) and self.isVowel(s[p2]):
                    p2 = p2 + 1
                    cur_len = cur_len + 1
                if cur_len > max_len:
                    max_len = cur_len
                p1 = p2 + 1
            else:
                p1 = p1 + 1
        return max_len

    def isVowel(self, letter):
        return letter.lower() in 'aeiou'