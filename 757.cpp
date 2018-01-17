// O(N^2), greedy
class Solution {
private:
	static bool compareInterval(vector<int> interval1, vector<int> interval2) {
		return (interval1[0] != interval2[0]) ? (interval1[0] < interval2[0]) : (interval1[1] > interval2[1]);
	}
public:
	int intersectionSizeTwo(vector<vector<int>>& intervals) {
		vector<int> todo(intervals.size(), 2);
		int result = 0;

		sort(intervals.begin(), intervals.end(), compareInterval);
		for (int i = intervals.size() - 1; i >= 0; i--) { // take from the last interval greedily
			int remain = todo[i];
			for (int j = 0; j < remain; j++) { // take the remain todo elements
				for (int k = 0; k <= i; k++) { // check if other intervals are chosen as well
					if (todo[k] > 0 && intervals[i][0] + j <= intervals[k][1])
						todo[k] --;
				}
				result ++;
			}
		}
		return result;
	}
};