// JavaScript Two Sum  One Pass Object Approach

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

const twoSum = (nums = [], target = 0) => {
    object = {}
    for(index = 0; index < nums.length; index++){
        complement = target - nums[index];
        if(complement in object)
            return [object[complement], index];
        object[nums[index]] = index;
    }
    return []
}

let target = 9;
let nums = [2, 11, 7, 15];
let result = twoSum(nums, target);
console.log(result);