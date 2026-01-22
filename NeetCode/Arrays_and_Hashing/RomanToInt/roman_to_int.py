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
            # Check if current numeral is smaller than next (subtractive notation: IV=4, IX=9, etc.)
            next_char = s[i+1] if i+1 < len(s) else None
            next_value = roman_numerals[next_char] if next_char else None
            print(f"Position {i}: '{s[i]}' (value: {roman_numerals[s[i]]}) vs next: '{next_char or 'N/A'}' (value: {next_value or 'N/A'}) - Checking if subtractive notation applies")
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                res -= roman_numerals[s[i]]
            else:
                res += roman_numerals[s[i]]

        return res
    
# Example usage:
solution = Solution()
print(solution.romanToInt("LVIII"))