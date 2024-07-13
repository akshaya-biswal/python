# Count Occurrences of Anagrams
from collections import Counter


def countAnagrams(text, pattern):
    # Initialize the result count
    result = 0

    # Lengths of the text and pattern
    n, k = len(text), len(pattern)

    # Frequency counter for the pattern
    pattern_count = Counter(pattern)

    # Frequency counter for the current window in the text
    window_count = Counter(text[: k - 1])
    print(pattern_count, window_count, text[: k - 1])

    # Iterate through the text with a sliding window
    for i in range(k - 1, n):
        # Add the new character to the window
        window_count[text[i]] += 1

        # Compare window counter with pattern counter
        if window_count == pattern_count:
            result += 1

        # Remove the character that is sliding out of the window
        window_count[text[i - k + 1]] -= 1
        if window_count[text[i - k + 1]] == 0:
            del window_count[text[i - k + 1]]

    return result


# Example usage:
print(countAnagrams("forxxorfxdofr", "for"))  #  output: 3
# print(countAnagrams("cbaebabacd", "abc"))  #  output: 2
# print(countAnagrams("abab", "ab"))  #  output: 3
