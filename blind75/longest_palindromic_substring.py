"""
Time of Start: 12:32 PM
Time at start solutioning: 12:33
Time at start coding: 12:43 => break at 12:50 => 1:23
time at testing:
time at submission:
"""
"""
longest palindromic substring.
global_max;
babad => 
just one counter => p1
1. from each => you try to expand on both sides; and stop whenever it stops being a palin
2. then you also see if two chars are same; that could also be the middle of a palin.
cbbd:
iamagirllrigamai
abacdcaba
p1 => for every p1 => check if it could be a single origin palindrome. 
p1 => check if either neighbor is the same. that could be a double original palin.

for until p1 end of len:
    check if signle origin:
         p1 -1, p1 + 1
    check if either neighbor is same;
         if p1 == p1 - 1:
            helper(p1-1, p1)
        elif p1 == p1+1
        helper(p1, p1+1)
    helper function: i1 and i2
    single origin(i, j)
"""
class Solution3:
    # abacdcaba
    def longest_palindromic_substring(self, s):
        longest = ""
        for i in range(len(s)): #i=1
            current_string = self.check_if_indices_make_palindrome(s, i-1, i+1) #0, 2
            longest = current_string if len(current_string) > len(longest) else longest
                
            if i-1 >= 0 and s[i] == s[i-1]:
                current_string = self.check_if_indices_make_palindrome(s, i-1, i)
                longest = current_string if len(current_string) > len(longest) else longest
            
            if i+1 < len(s) and s[i] == s[i+1]:
                current_string = self.check_if_indices_make_palindrome(s, i, i+1)
                longest = current_string if len(current_string) > len(longest) else longest
        return longest

    def check_if_indices_make_palindrome(self, s, i, j): #i=0 j=2
        while i >= 0 and j < len(s):
            if s[i] == s[j]:
                i = i-1 #i=-1
                j = j+1 #j=3
            else:
                break
        return s[i+1:j] #a

if __name__ == '__main__':
    s = Solution3()
    print(s.longest_palindromic_substring("iamagirlrigami"))
