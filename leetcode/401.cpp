class Solution {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> ans;
        if (num < 0 || num >= 9) // at most 3 lights on for hour, 5 lights on for minute
            return ans;
        vector<vector<string>> minute(6, vector<string>()), hour(4, vector<string>());
        vector<int> lights(1, 1);
        int flag = 0;
        // all hour possibility
        hour[0].push_back("0");
        for (int i = 1; i < 12; i++) {
            hour[lights[flag]].push_back(to_string(i));
            if (flag == lights.size() - 1) {
                vector<int> temp(lights);
                for (int j = 0; j < temp.size(); j++)
                    temp[j] += 1;
                lights.insert(lights.end(), temp.begin(), temp.end());
                flag = 0;
            }
            else
                flag ++;
        }
        
        lights = vector<int>(1, 1);
        flag = 0;
        // all minute possibility
        minute[0].push_back("00");
        for (int i = 1; i <= 59; i++) {
            if (i <= 9)
                minute[lights[flag]].push_back("0" + to_string(i));
            else
                minute[lights[flag]].push_back(to_string(i));
            if (flag == lights.size() - 1) {
                vector<int> temp(lights);
                for (int j = 0; j < temp.size(); j++)
                    temp[j] += 1;
                lights.insert(lights.end(), temp.begin(), temp.end());
                flag = 0;
            }
            else
                flag ++;
        }
        // collect all combinations
        for (int i = 0; i <= min(num, 3); i++) {
            if (num - i >= 0 && num - i <= 5) {
                for (string h : hour[i]) {
                    for (string m : minute[num - i])
                        ans.push_back(h + ":" + m);
                }
            }
        }
        return ans;
    }
};