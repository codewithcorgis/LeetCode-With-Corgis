  
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int index = 0; index < nums.length; index++) {
            for (int index2 = index + 1; index2 < nums.length; index2++) {
                if (nums[index2] == target - nums[index]) {
                    return new int[] { index, index2 };
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}