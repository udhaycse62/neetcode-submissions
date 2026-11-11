class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myhash=set()

        for num in nums:
            if num in myhash:
                return True
            myhash.add(num)
        return False


