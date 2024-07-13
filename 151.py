# Convert the string to a list of characters (to manipulate it in-place)
# Helper function to reverse a portion of the list in-place
# Reverse the entire list of characters
# Reverse each word in the reversed list
# --- First while loop: Skip Leading Spaces
# --- Second while loop: Find End of the Word
# --- Third while loop: Reverse the Word and assign End as Start index
# Join the characters to form the final string and split/join to handle multiple spaces


def reverseWords(s: str) -> str:
    chars = list(s)

    def reverse(lst, start, end):
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1

    n = len(chars)
    reverse(chars, 0, n - 1)

    start = 0
    while start < n:
        while start < n and chars[start] == " ":
            start += 1
        end = start
        while end < n and chars[end] != " ":
            end += 1
        reverse(chars, start, end - 1)
        start = end

    return " ".join("".join(chars).split())


s = "a good example"
print(reverseWords(s))  # Output: "example good a"
