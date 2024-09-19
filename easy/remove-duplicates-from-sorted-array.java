
class Solution {
/*
 * First Solution
 */
    private void remove(int[] nums, int pos, int last, int count) {
        for (int i = pos; i < last-count; i++) {
            nums[i] = nums[i+count];
        }
    }

    private int findNextDuplicate(int[] nums, int pos, int last, int val) {
        int count = 0;
        while (pos < last && nums[pos] == val) {
            count++; pos++;
        }
        return count;
    }

    public int removeDuplicates(int[] nums) {
        int lastValue = nums[0];
        int count = 0;
        int last = nums.length;
        int i = 1;

        while(i < last && i < nums.length) {
            if (lastValue == nums[i]) {
                int duplicates = findNextDuplicate(nums, i+1, last, nums[i]);
                duplicates++;
                remove(nums, i, last, duplicates);
                last -= duplicates; count += duplicates;
            } else {
                lastValue = nums[i];
                i++;
            }
        }

        return nums.length - count;
    }
/*
 * Second Solution
 */
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}


