class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxVol = 0, left = 0, right = heights.size() - 1;

        while(left < right){
            int curVol = (right - left) * min(heights[left], heights[right]);

            maxVol = max(curVol, maxVol);

            if(heights[left] <= heights[right]) left++;
            else if(heights[right] <= heights[left]) right--;
        }

        return maxVol;
    }
};
