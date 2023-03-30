class Solution {
public:
    int lengthOfLastWord(string s) {
        int start = -1;
        int size = 0;
        for (int i = s.size() - 1; i > -1; i--) {
            if (start != -1) {
                if (s[i] != ' ') {
                    size++;
                } else {
                    return size + 1;
                }    
            }
            if (start == -1 and s[i] != ' ') {
                start = i;
            }  
        } 
        return size + 1;
    }
};
