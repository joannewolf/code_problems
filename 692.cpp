class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        // count words
        map<string, int> counts;
        for (string s : words) {
        	if (counts.find(s) == counts.end())
        		counts[s] = 1;
        	else
        		counts[s] ++;
        }
        // find top k frequent words with heap
        auto mycompare = [&](const pair<string,int>& a, const pair<string,int>& b) {
            return (a.second > b.second || (a.second == b.second && a.first < b.first));
        };
        priority_queue< pair<string, int>, vector<pair<string, int>>, decltype(mycompare) > pq(mycompare);

        for (auto c : counts) {
        	pq.emplace(c.first, c.second);
        	if (pq.size() > k)
        		pq.pop();
        }

        // collect output
        vector<string> result;
        while (!pq.empty()) {
        	result.insert(result.begin(), pq.top().first);
        	pq.pop();
        }
        return result;
    }
};