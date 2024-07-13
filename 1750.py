def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1

    while left < right and s[left] == s[right]:
        char = s[left]

        while left <= right and s[left] == char:
            left += 1

        while left <= right and s[right] == char:
            right -= 1

    return right - left + 1 if left <= right else 0


# Example usage:
print(minimumLength("aa"))  # output: 0
print(minimumLength("ca"))  # output: 2
print(minimumLength("cabaabac"))  # output: 0
print(minimumLength("aabccabba"))  # output: 3
