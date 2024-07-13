def reverseVowels(str: str) -> str:
    vowels = "aeiouAEIOU"
    str_list = list(str)

    left = 0
    right = len(str) - 1

    while left < right:
        if str_list[left] not in vowels:
            left += 1
        elif str_list[right] not in vowels:
            right -= 1
        else:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1

    return "".join(str_list)


# Example usage:
str = "hello"
print(reverseVowels(str))  # "holle"

str = "leetcode"
print(reverseVowels(str))  # "leotcede"
