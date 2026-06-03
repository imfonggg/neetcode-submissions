class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int r = 0; r < 9; r++){
            unordered_set<char> Row;
            unordered_set<char> Col;
            for(int c = 0; c < 9; c++)
            {
                if(Row.count(board[r][c]) || Col.count(board[c][r])) return false;

                if(board[r][c] != '.'){
                    Row.insert(board[r][c]);
                }

                if(board[c][r] != '.'){
                    Col.insert(board[c][r]);
                }
            }
        }

        for (int square = 0; square < 9; square++) {
            unordered_set<char> seen;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }
        return true;
    }
};
