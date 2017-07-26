class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        if (A.size() == 0)
        	return 0;
        sort(A.begin(), A.end());
        sort(B.begin(), B.end());
        sort(C.begin(), C.end());
        sort(D.begin(), D.end());
        // count all the elements in vectors
        map<int, int> countA, countB, countC, countD, abSum;
        int result = 0;
        for (int i = 0; i < A.size(); i++) {
        	if (countA.find(A[i]) == countA.end())
        		countA[A[i]] = 1;
        	else
        		countA[A[i]] ++;
        }
        for (int i = 0; i < B.size(); i++) {
        	if (countB.find(B[i]) == countB.end())
        		countB[B[i]] = 1;
        	else
        		countB[B[i]] ++;
        }
        for (int i = 0; i < C.size(); i++) {
        	if (countC.find(C[i]) == countC.end())
        		countC[C[i]] = 1;
        	else
        		countC[C[i]] ++;
        }
        for (int i = 0; i < D.size(); i++) {
        	if (countD.find(D[i]) == countD.end())
        		countD[D[i]] = 1;
        	else
        		countD[D[i]] ++;
        }

        for (pair<int, int> a : countA) {
        	for (pair<int, int> b : countB) {
        		int temp = a.first + b.first;
        		if (abSum.find(temp) == abSum.end())
        			abSum[temp] = a.second * b.second;
        		else
        			abSum[temp] += (a.second * b.second);
        	}
        }
        for (pair<int, int> c : countC) {
        	for (pair<int, int> d : countD) {
        		int temp = 0 - c.first - d.first;
        		if (abSum.find(temp) != abSum.end())
        			result += (abSum[temp] * c.second * d.second);
        	}
        }

        return result;
    }
};