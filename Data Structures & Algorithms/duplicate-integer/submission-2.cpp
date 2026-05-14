class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

    unordered_map <int,int> dict;

    for (int i=0; i<nums.size(); i++){
        if (dict[nums[i]] == 1){
            return true;
        }
        else {
            dict[nums[i]] = 1;
        }
    }
    return false;
        
    }
};