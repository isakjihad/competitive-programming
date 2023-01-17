class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if x==0: return 0
            if n==0: return 1
            resul=helper(x,n//2)
            resul=resul*resul
            return x*resul if n%2 else resul
        resul= helper(x,abs(n))
        return resul if n >=0 else 1/resul