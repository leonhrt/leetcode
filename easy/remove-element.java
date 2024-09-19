class Solution {
    private void reorder(int[] nums, int pos, int last) {
        for (int i = pos; i < last - 1; i++) {
            nums[i] = nums[i + 1];
        }
    }

    public int removeElement(int[] nums, int val) {
        int count = 0;
        int last = nums.length;
        int i = 0;
        while (i < last) {
            if (nums[i] == val) {
                reorder(nums, i, last);
                last--;
                count++;
            } else {
                i++;
            }
        }

        return nums.length - count;
    }
}
