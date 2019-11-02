class Solution {
public:
	bool canPlaceFlowers(vector<int>& flowerbed, int n) {
		int place = 0, spaceCount = 0;

		flowerbed.insert(flowerbed.begin(), 0);
		flowerbed.emplace_back(0);
		flowerbed.emplace_back(1);
		for (int i = 0; i < flowerbed.size(); i++) {
			if (flowerbed[i] == 0) {
				spaceCount ++;
			}
			else {
				place += ((spaceCount - 1) / 2);
				spaceCount = 0;
			}
		}

		return (place >= n);
	}
};

class Solution {
public:
	bool canPlaceFlowers(vector<int>& flowerbed, int n) {
		int place = 0;

		if (flowerbed[0] == 0 && flowerbed[1] == 0) {
			flowerbed[0] = -1;
			place ++;
		}
		for (int i = 1; i < flowerbed.size() - 1; i++) {
			if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
				flowerbed[i] = -1;
				place ++;
			}
		}
		if (flowerbed[flowerbed.size() - 1] == 0 && flowerbed[flowerbed.size() - 2] == 0) {
			flowerbed.back() = -1;
			place ++;
		}

		return (place >= n);
	}
};