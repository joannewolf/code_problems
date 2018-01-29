class Solution {
private:
	vector<string> basicWords, tenWords;
	string getSmallNumberWords(int num) {
		// guarantee the number input < 1000
		string result = "";
		if (num / 100 != 0) {
			result += (basicWords[num / 100] + " ");
			result += "Hundred ";
			num %= 100;
		}
		if (num >= 20) {
			result += (tenWords[num / 10] + " ");
			if (num % 10 != 0)
				result += (basicWords[num % 10] + " ");
		}
		else if (num != 0)
			result += (basicWords[num] + " ");

		return result;
	}
public:
	string numberToWords(int num) {
		if (num == 0)
			return "Zero";

		string ans;
		basicWords = vector<string>({"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"});
		tenWords = vector<string>({"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"});
		if (num >= 1000000000) {
			ans = ans + getSmallNumberWords(num / 1000000000) + "Billion ";
			num %= 1000000000;
		}

		if (num >= 1000000) {
			ans = ans + getSmallNumberWords(num / 1000000) + "Million ";
			num %= 1000000;
		}

		if (num >= 1000) {
			ans = ans + getSmallNumberWords(num / 1000) + "Thousand ";
			num %= 1000;
		}

		ans = ans + getSmallNumberWords(num);
		ans.pop_back();
		return ans;
	}

};