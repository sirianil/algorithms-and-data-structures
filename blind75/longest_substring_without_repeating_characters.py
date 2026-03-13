"""
Time of Start: 11:31 AM
Time at start solutioning: 11:32
Time at start coding: 11:40
time at testing: 11:48
time at submission:
"""
"""
Alogrithm Discussion:
"abcabcbb"
p1 = 0
p2 = 1;
current_set = {s[p1]};
global_max;
while p2 < len and p1 < p2: => p2 = 2;
    increment p2 until we find something that is already in set
        keep adding p2 to set
        increment p2
    update global_mx => 3
    remove p1 from set => b,c
    clear current len
"""
"""
Review:Overall good on time: 30 minutes.
could have been faster but because this is in the beginning it is still okay.
missed a couple of edge cases and could not easily debug it either.
so pay attention to the edge cases more.
"""


class Solution1:
    def find_longest_substring_without_repeating_characters(self, s):
        p1 = 0
        p2 = 1
        current_set = {s[p1]}
        global_max = 0

        while p2 < len(s) and p1 <= p2:
            while p2 < len(s) and s[p2] not in current_set:
                current_set.add(s[p2])
                p2 += 1
            if global_max < len(current_set):
                global_max = len(current_set)
            current_set.remove(s[p1])
            p1 += 1
        if global_max < len(current_set):
            global_max = len(current_set)            
        return global_max

if __name__ == '__main__':
    s = Solution1()
    print(s.find_longest_substring_without_repeating_characters("pwwkew"))
