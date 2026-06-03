class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0, right = s.length() - 1;

        while(left < right)
        {
            while(left < right && !isASCII(s[left]))
            {
                left++;
            }

            while(right > left && !isASCII(s[right]))
            {
                right--;
            }

            if(tolower(s[left]) != tolower(s[right])) return false;

            left++;
            right--;
        }

        return true;
    }

    bool isASCII(char c){
        return ((c >= 'A' && c <= 'Z') ||
                (c >= 'a' && c <= 'z') ||
                (c >= '0' && c <= '9'));
    }
};
