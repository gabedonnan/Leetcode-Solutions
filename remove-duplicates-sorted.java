class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> map = new HashSet<Integer>();
        int shift = 0;
        for (int i = 0; i < nums.length; i++) {
            if (map.contains(nums[i + shift])) {
                for (int j = (i + shift); j < nums.length - 1; j++) {
                    nums[j] = nums[j+1];
                }
                shift--;
            } else {
                map.add(nums[i + shift]);
            }
        } 
        return nums.length + shift;
    }
}
