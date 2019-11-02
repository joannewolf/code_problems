class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> points(2, 0);
        int totalPoints = 0;

        for (string s : ops) {
        	if (s == "+") {
        		points.emplace_back(points[points.size() - 1] + points[points.size() - 2]);
        		totalPoints += points.back();
        	}
        	else if (s == "D") {
        		points.emplace_back(points.back() * 2);
        		totalPoints += points.back();
        	}
        	else if (s == "C") {
        		totalPoints -= points.back();
        		points.pop_back();
        	}
        	else {
        		int num = stoi(s);
        		points.emplace_back(num);
        		totalPoints += num;
        	}
        }

        return totalPoints;
    }
};