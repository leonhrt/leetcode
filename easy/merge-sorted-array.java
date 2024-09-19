class Solution {
    private void addAndReorder(int[] nums, int num, int pos, int size) {
        for (int i = pos; i < size; i++) {
            int aux = nums[i];
            nums[i] = num;
            num = aux;
        }
    }

    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if (m == 0) {
            System.arraycopy(nums2, 0, nums1, 0, m+n);
            return;
        } else if (n == 0) {
            return;
        }

        int start_n = m;
        int j = 0;
        int mn = m+n;
        for (int i = 0; i < start_n && start_n < mn; i++) {
            if (nums2[j] < nums1[i]) {
                addAndReorder(nums1, nums2[j], i, mn);
                j++; start_n++;
            }
        }

        while (start_n < mn) {
            nums1[start_n] = nums2[j];
            j++; start_n++;
        }
    }
}
