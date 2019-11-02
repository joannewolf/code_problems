class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result (1, 1), temp;
        for (int i = 0; i < rowIndex; i++) {
            temp.push_back(1);
            for (int j = 0; j < result.size() - 1; j++)
                temp.push_back(result[j] + result[j + 1]);
            temp.push_back(1);
            result = temp;
            temp.clear();
        }
        return result;
    }
};