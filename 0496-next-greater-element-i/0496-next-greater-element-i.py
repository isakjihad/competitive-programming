class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx={n:i for i ,n in enumerate(nums1)}
        resul=[-1]*len(nums1)
        stack=[]
        for i in range(len(nums2)):
            curr=nums2[i]
            while stack and curr > stack[-1]:
                val=stack.pop()
                idx=nums1Idx[val]
                resul[idx]=curr
            if curr in nums1Idx:
                stack.append(curr)
        return resul