# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [2, 7]
# Explanation: Because 2 + 7 == 9, we return [2, 7]

def pair_sum(arr, x):
    """
    A function that returns two numbers present in an array such that they add up to
    the target value
    """
    # Creating a hashmap
    seen = {}
    for num in arr:
        # Fetching and adding the difference between target and current value to hashmap
        diff = x - num
        if diff in seen:
            return [seen.get(diff, 0), num]
        seen[num] = num
    return []

# Time complexity - O(n)
# Space complexity - O(n) due to hashmap


# Some test cases
arr, x = [2, 7, 11, 15], 9
assert(pair_sum(arr, x)) == [2, 7]
arr, x = [1, 9, 13, 20, 47], 10
assert(pair_sum(arr, x)) == [1, 9]
arr, x = [], 5
assert(pair_sum(arr, x)) == []
