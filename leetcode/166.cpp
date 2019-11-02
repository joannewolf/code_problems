class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
    	if (numerator == 0)
    		return "0";
    	
        bool symbol = ((numerator > 0) == (denominator > 0));

        string result;
        if (!symbol)
        	result += "-";

    	long long longNumerator = abs((long long)numerator);
    	long long longDenominator = abs((long long)denominator);
        result += to_string(longNumerator / longDenominator);
        longNumerator -= (longDenominator * (longNumerator / longDenominator));

        if (longNumerator == 0)
        	return result;
        else {
        	result += ".";
        	map<long long, int> numerators;
        	string decimals;
        	while (longNumerator != 0) {
        		longNumerator *= 10;
                if (numerators.find(longNumerator) != numerators.end()) {
                    decimals.insert(decimals.begin() + numerators[longNumerator], '(');
                    decimals += ")";
                    result += decimals;
                    return result;
                }
        		numerators[longNumerator] = decimals.length();
        		decimals += to_string(longNumerator / longDenominator);
        		longNumerator -= (longDenominator * (longNumerator / longDenominator));
        	}
        	result += decimals;
        	return result;
        }
    }
};