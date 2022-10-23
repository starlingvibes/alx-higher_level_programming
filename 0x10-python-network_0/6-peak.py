#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    n = len(list_of_integers)
    nums = list_of_integers
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if ((mid == n - 1 or nums[mid] > nums[mid + 1]) and
                (mid == 0 or nums[mid] > nums[mid - 1])):
            return nums[mid]
        elif ((mid == n - 1 or nums[mid] < nums[mid + 1]) and
                (mid == 0 or nums[mid] > nums[mid - 1])):
            left = mid + 1
        else:
            right = mid - 1
