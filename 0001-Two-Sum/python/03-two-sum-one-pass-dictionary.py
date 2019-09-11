# Python Two Sum One Pass Dictionary Approach 

from typing import List

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        
        """
        :type nums: List[int]
        :type target: int
        :return type: List[int]
        """

        dictionary = {}
        for index in range(0, len(nums)):
            complement = target - nums[index]
            if(complement in dictionary):
                return [dictionary[complement], index]
            dictionary[nums[index]] = index
        return []
    
if __name__ == "__main__":
    target = 9
    nums = [2, 11, 7, 15]
    result = Solution().twoSum(nums, target) 
    print(result)
