class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        stack<pair<int, int>> stack;
        int maxArea = 0;

        for(int i = 0; i < heights.size(); i++){
            int start = i;
            while(!stack.empty() && stack.top().second > heights[i]){
                pair<int,int> top = stack.top();
                int ind = top.first;
                int h = top.second;

                maxArea = max(maxArea, h * (i - ind));

                start = ind;
                stack.pop();
            }
            stack.push({start, heights[i]});
        }

        while(!stack.empty()){
            int ind = stack.top().first;
            int h = stack.top().second;

            maxArea = max(maxArea, h * (static_cast<int>(heights.size()) - ind));
            stack.pop();
        }
        return maxArea;
    }
};
