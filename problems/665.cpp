/*

Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

*/

class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        
        const int ONE_MOVE = 1;
        int curMin = INT_MAX;
        int curMax = INT_MIN;
        stack<int> lookbackMin;
        queue<int> lookforwardMax;
        int numMinModify = 0;
        int numMaxModify = 0;
        
        for (int idx = nums.size() - 1; idx >= 0; idx--) {
            if (curMin > nums[idx]) {
                curMin = nums[idx];
            }
            lookbackMin.push(curMin);
        }
        for (int idx = 0; idx < nums.size(); idx++) {
            if (nums[idx] > lookbackMin.top()) {
                numMinModify += 1;
            }
            lookbackMin.pop();
        }
        
        for (int idx = 0; idx < nums.size(); idx++) {
            if (curMax < nums[idx]) {
                curMax = nums[idx];
            }
            lookforwardMax.push(curMax);
        }
        for (int idx = 0; idx < nums.size(); idx++) {
            if (nums[idx] < lookforwardMax.front()) {
                numMaxModify += 1;
            }
            lookforwardMax.pop();
        }
        
        if (numMinModify > ONE_MOVE and numMaxModify > ONE_MOVE) {
            return false;
        } else {
            return true;
        }
    }
};