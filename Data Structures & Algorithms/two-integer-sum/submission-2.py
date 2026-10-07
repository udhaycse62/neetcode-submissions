class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myhashmap = {}

        for i, n in enumerate(nums):
            myhashmap[n]=i

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in myhashmap and myhashmap[diff]!= i :
                return [i, myhashmap[diff]]

        