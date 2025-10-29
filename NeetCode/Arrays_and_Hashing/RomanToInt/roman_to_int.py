class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                res -= roman_numerals[s[i]]
            else:
                res += roman_numerals[s[i]]

        return res
    
# Example usage:
solution = Solution()
print(solution.romanToInt("LVIII"))