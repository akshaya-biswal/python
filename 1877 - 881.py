def minPairSum(nums):
    # Sort the array
    nums.sort()

    # Initialize two pointers
    left = 0
    right = len(nums) - 1

    # Initialize the variable to store the maximum pair sum
    max_pair_sum = 0

    # Iterate while left pointer is less than right pointer
    while left < right:
        # Calculate the pair sum
        pair_sum = nums[left] + nums[right]
        # Update the maximum pair sum
        max_pair_sum = max(max_pair_sum, pair_sum)
        # Move the pointers
        left += 1
        right -= 1

    return max_pair_sum


# Example usage:
print(minPairSum([3, 5, 6, 7]))  # Output: 10
print(minPairSum([3, 5, 4, 2, 4, 6]))  # Output: 8
print(minPairSum([3, 5, 2, 3]))  # Output: 7
