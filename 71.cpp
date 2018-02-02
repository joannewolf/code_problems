class Solution {
public:
	string simplifyPath(string path) {
		if (path.empty())
			return "";

		vector<string> level;
		string temp = "";

		path += '/';
		for (char c : path) {
			if (c == '/') {
				if (temp == ".." && !level.empty())
					level.pop_back();
				else if (!temp.empty() && temp != "." && temp != "..")
					level.emplace_back(temp);
				temp.clear();
			}
			else
				temp += c;
		}

		if (level.empty())
			return "/";
		else {
			string result = "";
			for (string s : level)
				result += ("/" + s);
			return result;
		}
	}
};