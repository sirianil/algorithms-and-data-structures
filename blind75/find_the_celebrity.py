# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

'''
T1: 
n = 2:
0 and 1: knows(0,1) -> yes; 0 cannot be C
         knows(1,0) -> no;

0, 1, 2, 3, 4, 5: 
possible_celebrity = [0,1,2....n-1]
for i in range(0 to n-1):
    for c in possible_celebrity:
        if not knows(i, c):
            possible_celebrity.remove(c)
'''
class Solution:
    def knows(self, i, j):
        self.graph = [[1,1],[1,1]]
        return True if self.graph[i][j] == 1 else False
    
    def findCelebrity(self, n: int) -> int:
        celebCandidate = 0
        
        for i in range(n):
            not_celeb = []
            for c in possible_celebrity:
                if not self.knows(i, c):
                    not_celeb.append(c)
            for n_c in not_celeb:
                possible_celebrity.remove(n_c)

        if len(possible_celebrity):
            return possible_celebrity.pop()
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.findCelebrity(2))