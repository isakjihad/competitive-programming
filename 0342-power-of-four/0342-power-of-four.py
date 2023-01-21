class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <=0 :
            return False
        if n & n -1!=0:
            return False
        b=bin(n)[::-1]
        p=b.index("1")
        return p%2 ==0