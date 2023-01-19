from sortedcontainers import SortedList
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        s1=SortedList(x+1 for x in range(n))
        curr=len(s1)-1
        while len(s1)>1:
            curr=(curr+k)%len(s1)
            s1.remove(s1[curr])
            curr-=1
            curr%=len(s1)
        return s1[0]
       
        
