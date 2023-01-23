class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        std::vector<int> trusters;
        std::vector<int> trustees;
        for (const std::vector<int>& h: trust) {
            //std::cout << h[0] << std::endl << h[1] << std::endl;
            trusters.push_back(h[0]);
            trustees.push_back(h[1]);
        }
        
        for (int i = 1; i <= n; i++) {
            //std::cout << i << "\n";
            if (std::count(trusters.begin(), trusters.end(), i)){
                continue;
            } else {
                //std::cout << trustees[i-1] << "TRUSTEE" << "\n";
                if (std::count(trustees.begin(), trustees.end(), i) == n-1){
                    return i;
                }
            }
        }
        return -1;
    }
};
