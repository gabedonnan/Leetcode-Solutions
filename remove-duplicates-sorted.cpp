class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int numSize = nums.size();
        if (numSize == 0) {
            return 0;
        }
        int shift = 0;
        int prev = nums[0];
        for (int i = 0; i < numSize; i++) {
            if (i != 0 && nums[i-shift] == prev) {
                nums.erase(nums.begin()+(i-shift));
                shift++;
            }
            prev = nums[i-shift];
        }
        return nums.size();
    }
};
