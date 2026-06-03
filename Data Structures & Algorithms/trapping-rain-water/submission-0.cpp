class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;

        int left = 0, right = height.size() - 1, res = 0;
        int maxLeft = height[left], maxRight = height[right];

        while (left < right){
            if(maxLeft < maxRight){
                left++;
                maxLeft = max(maxLeft, height[left]);
                res += maxLeft - height[left];
            }
            else
            {
                right--;
                maxRight = max(maxRight, height[right]);
                res+= maxRight - height[right];
            }
        }
        return res;
    }
};