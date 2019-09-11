// JavaScript Two Sum Bruteforce Approach

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 const twoSum = (nums = [], target = 0) => {
    for(let index = 0; index < nums.length; index++){
        for(let index2 = index + 1; index2 < nums.length; index2++){
            if(nums[index2] === target - nums[index]){
                return [index, index2];
            }
        }
    }
 }

 let target = 9;
 let nums = [2, 11, 7, 15];
 let result = twoSum(nums, target);
 console.log(result);