# Split the string into words
# Reverse the list of words
# Join the reversed list of words into a single string


def reverseWords(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    reversed_string = " ".join(reversed_words)
    return reversed_string


# Example usage:
print(reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(reverseWords("  hello world  "))  # Output: "world hello"
print(reverseWords("a good   example"))  # Output: "example good a"
