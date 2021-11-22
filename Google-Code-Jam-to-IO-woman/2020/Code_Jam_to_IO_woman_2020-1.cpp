// Interleaved Output: Part 1
// https://codingcompetitions.withgoogle.com/codejamio/round/000000000019ff03/00000000001b5e88

#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    
    cin >> T;
    for (int t = 0; t < T; t++) {
        // get input for each case
        string S;
        cin >> S;
        
        int ans = 0;
        int Icount = 0, icount = 0;
        // If see 'O', match with 'I' first; if see 'o', match with 'o' first
        for (char c : S) {
            switch (c) {
                case 'I':
                    Icount ++;
                    break;
                case 'i':
                    icount ++;
                    break;
                case 'O':
                    if (Icount > 0) {
                        ans ++;
                        Icount --;
                    }
                    else
                        icount --;
                    break;
                case 'o':
                    if (icount > 0)
                        icount --;
                    else
                        Icount --;
                    break;
                default:
                    break;
            }
        }

        cout << "Case #" << t + 1 << ": " << ans << endl;
    }
    
    return 0;
}