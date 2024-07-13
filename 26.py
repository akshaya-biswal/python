# 1. Initialize the index for the unique element: unique_index
# 2. Iterate through the array starting from the second element
# 3. If the current element is different from the unique element
# 4. Move the unique index forward and update the value: nums[unique_index] = nums[i]
# 5. The length of the array without duplicates: unique_index + 1


def removeDuplicates(nums):
    if not nums:
        return 0

    unique_index = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_index]:
            unique_index += 1
            nums[unique_index] = nums[i]

    return unique_index + 1


nums = [1, 1, 2]
length = removeDuplicates(nums)
print(nums[:length])  # Output: [1, 2]

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length = removeDuplicates(nums)
print(nums[:length])  # Output: [0, 1, 2, 3, 4]
