class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        a=Counter(nums)
        op=0
        see=set()
        for i in a:
            if i not in see and (k-i) in a:
                if i==(k-i):
                    op+=a[i]//2 
                else:
                    
                    op +=min(a[i],a[k-i])
                see.add(i)
                see.add(k-i)
        return op