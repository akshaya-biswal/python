def numOfSubsequence(nums, target):
    MOD = 10**9 + 7  # Define the modulo constant

    # Sort the array
    nums.sort()
    n = len(nums)

    # Pre-compute powers of 2 up to the length of nums
    powers = [1] * n
    for i in range(1, n):
        powers[i] = powers[i - 1] * 2

    left, right = 0, n - 1
    result = 0

    while left <= right:
        if nums[left] + nums[right] <= target:
            result += powers[right - left]
            result %= MOD  # Apply modulo to keep result manageable
            left += 1
        else:
            right -= 1

    return result


# Example usage:
print(numOfSubsequence([3, 5, 6, 7], 9))  # Output: 4
print(numOfSubsequence([3, 3, 6, 8], 10))  # Output: 6
print(numOfSubsequence([2, 3, 3, 4, 6, 7], 12))  # Output: 61
