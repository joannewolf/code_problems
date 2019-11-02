#include <math.h>
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int left = max(A, E);
        int right = min(C, G);
        int bottom = max(B, F);
        int top = min(D, H);
        int overlapped = (left >= right || bottom >= top) ? 0 : ((right - left) * (top - bottom));
        return (C - A) * (D - B) + (G - E) * (H - F) - overlapped;
    }
};