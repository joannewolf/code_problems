// O(N), count total area & match every corner
class Solution {
public:
	bool isRectangleCover(vector<vector<int>>& rectangles) {
		int left = INT_MAX, down = INT_MAX, right = INT_MIN, up = INT_MIN;
		int area = 0;
		unordered_set<string> corners;

		for (vector<int> &rectangle : rectangles) {
			left = min(left, rectangle[0]);
			down = min(down, rectangle[1]);
			right = max(right, rectangle[2]);
			up = max(up, rectangle[3]);

			area += ((rectangle[2] - rectangle[0]) * (rectangle[3] - rectangle[1]));

			string corner;
			corner = to_string(rectangle[0]) + "," + to_string(rectangle[1]);
			if (corners.find(corner) == corners.end())
				corners.insert(corner);
			else
				corners.erase(corner);

			corner = to_string(rectangle[0]) + "," + to_string(rectangle[3]);
			if (corners.find(corner) == corners.end())
				corners.insert(corner);
			else
				corners.erase(corner);

			corner = to_string(rectangle[2]) + "," + to_string(rectangle[1]);
			if (corners.find(corner) == corners.end())
				corners.insert(corner);
			else
				corners.erase(corner);

			corner = to_string(rectangle[2]) + "," + to_string(rectangle[3]);
			if (corners.find(corner) == corners.end())
				corners.insert(corner);
			else
				corners.erase(corner);
		}

		if (corners.find(to_string(right) + "," + to_string(down)) == corners.end() || 
			corners.find(to_string(right) + "," + to_string(up)) == corners.end() || 
			corners.find(to_string(left) + "," + to_string(down)) == corners.end() || 
			corners.find(to_string(left) + "," + to_string(up)) == corners.end() || 
			corners.size() != 4)
			return false;

		return (area == (right - left) * (up - down));
	}
};

// O(N^2logN), count rows' ranges and check if there's intersection [TLE]
class Solution {
private:
	static bool compareRanges(pair<int, int> range1, pair<int, int> range2) {
		return (range1.first != range2.first) ? (range1.first < range2.first) : (range1.second < range2.second);
	}
public:
	bool isRectangleCover(vector<vector<int>>& rectangles) {
		int left = INT_MAX, down = INT_MAX, right = INT_MIN, up = INT_MIN;

		for (vector<int> &rectangle : rectangles) {
			left = min(left, rectangle[0]);
			down = min(down, rectangle[1]);
			right = max(right, rectangle[2]);
			up = max(up, rectangle[3]);
		}

		vector<vector<pair<int, int>>> rows(up - down);
		for (vector<int> &rectangle : rectangles) {
			for (int i = rectangle[1] - down; i < rectangle[3] - down; i++)
				rows[i].emplace_back(make_pair(rectangle[0], rectangle[2]));
		}
		for (vector<pair<int, int>> &ranges : rows) {
			sort(ranges.begin(), ranges.end(), compareRanges);
			if (ranges.front().first != left || ranges.back().second != right)
				return false;
			for (int i = 1; i < ranges.size(); i++) {
				if (ranges[i - 1].second != ranges[i].first)
					return false;
			}
		}
		return true;
	}
};

// count rows and columns [WA]
class Solution {
public:
	bool isRectangleCover(vector<vector<int>>& rectangles) {
		int left = INT_MAX, down = INT_MAX, right = INT_MIN, up = INT_MIN;

		for (vector<int> &rectangle : rectangles) {
			left = min(left, rectangle[0]);
			down = min(down, rectangle[1]);
			right = max(right, rectangle[2]);
			up = max(up, rectangle[3]);
		}

		vector<int> rows(up - down, 0), columns(right - left, 0);
		for (vector<int> &rectangle : rectangles) {
			for (int i = rectangle[0] - left; i < rectangle[2] - left; i++)
				columns[i] += (rectangle[3] - rectangle[1]);
			for (int i = rectangle[1] - down; i < rectangle[3] - down; i++)
				rows[i] += (rectangle[2] - rectangle[0]);
		}

		for (int &i : rows) {
			if (i != right - left)
				return false;
		}
		for (int &i : columns) {
			if (i != up - down)
				return false;
		}

		return true;
	}
};

// merge rectangles until become one whole rectangle [WA]
class Solution {
public:
	bool isRectangleCover(vector<vector<int>>& rectangles) {
		while (rectangles.size() > 1) {
			bool canMerge = false;
			for (int i = 0; i < rectangles.size(); i++) {
				for (int j = i + 1; j < rectangles.size(); j++) {
					if ((rectangles[i][0] == rectangles[j][0] && rectangles[i][2] == rectangles[j][2] && (rectangles[i][1] == rectangles[j][3] || rectangles[i][3] == rectangles[j][1])) || 
						(rectangles[i][1] == rectangles[j][1] && rectangles[i][3] == rectangles[j][3] && (rectangles[i][0] == rectangles[j][2] || rectangles[i][2] == rectangles[j][0]))) {
						// printf("[%d, %d, %d, %d] + [%d, %d, %d, %d]", 
							// rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3], 
							// rectangles[j][0], rectangles[j][1], rectangles[j][2], rectangles[j][3]);
						
						rectangles[i][0] = min(rectangles[i][0], rectangles[j][0]);
						rectangles[i][1] = min(rectangles[i][1], rectangles[j][1]);
						rectangles[i][2] = max(rectangles[i][2], rectangles[j][2]);
						rectangles[i][3] = max(rectangles[i][3], rectangles[j][3]);
						// printf(" -> [%d, %d, %d, %d]\n", 
							// rectangles[i][0], rectangles[i][1], rectangles[i][2], rectangles[i][3]);
						rectangles.erase(rectangles.begin() + j);
						canMerge = true;
						i --;
						break;
					}
				}
			}
			if (!canMerge)
				return false;
		}
		return true;
	}
};