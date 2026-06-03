class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size(), cols = matrix[0].size();
        int top = 0, bot = rows - 1;

        while (top <= bot){
            int midRow = (top + bot) / 2;
            if(target < matrix[midRow][0]){
                bot = midRow - 1;
            }
            else if (target > matrix[midRow][cols - 1]){
                top = midRow + 1;
            }
            else break;
        }

        if(!(top <= bot)) return false;

        int midRow = (top + bot) / 2;
        int l = 0, r = cols - 1;

        while (l <= r){
            int m = (l + r) / 2;
            if(target > matrix[midRow][m]){
                l = m + 1;
            } 
            else if (target < matrix[midRow][m]){
                r = m - 1;
            } 
            else{
                return true;
            }
        }

        return false;
    }
};
