class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        if (points.size() < 3)
            return 0;
        int count = 0;
        // for each point i, find the distances between i and all other points
        // and count the number of boomerangs with its center i
        for (int i = 0; i < points.size(); i++) {
            map<int, int> distances;
            for (int j = 0; j < points.size(); j++) {
                if (i == j)
                    continue;
                int temp = (points[i].first - points[j].first) * (points[i].first - points[j].first) + (points[i].second - points[j].second) * (points[i].second - points[j].second);
                if (distances.find(temp) == distances.end())
                    distances[temp] = 1;
                else
                    distances[temp] ++;
            }
            for (map<int, int>::iterator it = distances.begin(); it != distances.end(); it++)
                count += ((it -> second) * ((it -> second) - 1));
            distances.clear();
        }

        return count;
    }
};