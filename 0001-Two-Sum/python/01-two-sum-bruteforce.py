# Python Two Sum Bruteforce Approach

from typing import List

class Solution:
    def twoSum(self, nums:List[int], target:int) -> List[int]:
        
        """
        :type nums: List[int]
        :type target: int
        :return type: List[int]
        """

        for index in range(0, len(nums)):
            for index2 in range(index + 1, len(nums)):
                if(nums[index2] == target - nums[index]):
                    return [index, index2]
        return [] 



if __name__ == "__main__":
    target = 9
    nums = [2, 11, 7, 15]
    result = Solution().twoSum(nums, target) 
    print(result)
