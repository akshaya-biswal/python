def numberOfGoodPartitions(nums):
    M = 10**9 + 7
    n = len(nums)

    # HashMap to store the last occurrence of each number
    last_index = {num: i for i, num in enumerate(nums)}

    # Initialize pointers and result
    i = 0
    j = last_index[nums[0]]
    result = 1

    # Iterate through the array
    while i < n:
        if i > j:  # Found a partition point
            result = (result * 2) % M

        # Update j to the farthest last occurrence seen so far
        j = max(j, last_index[nums[i]])
        i += 1

    return result


# Example usage:
print(numberOfGoodPartitions([1, 2, 3, 4]))  # Example output
print(numberOfGoodPartitions([1, 2, 3, 1, 2, 3]))  # Example output
