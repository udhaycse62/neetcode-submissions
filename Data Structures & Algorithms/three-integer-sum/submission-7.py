class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , num in enumerate(nums):
            if num>0:
                break
            
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            left,right = i+1, len(nums)-1

            while left < right:
                Sum = nums[i] + nums[left] + nums[right]

                if Sum > 0:
                    right-=1
                
                elif Sum < 0:
                    left+=1
                
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    right-=1
                    left+=1

                    while nums[left] == nums[left-1] and left < right:
                        left+=1
        return res

