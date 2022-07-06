#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or len(roman_string) == 0:
        return 0
    roman_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                    'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string) - 1):
        first = roman_arabic[roman_string[i]]
        second = roman_arabic[roman_string[i + 1]]
        if first < second:
            result -= first
        else:
            result += first
    result += roman_arabic[roman_string[len(roman_string) - 1]]
    return result
