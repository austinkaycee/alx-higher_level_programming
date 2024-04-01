def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - A peak element from the list.
    """

    # Check if the list is empty
    if not list_of_integers:
        return None

    # Perform binary search to find a peak
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if the mid element is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Check if the mid element is greater than its left neighbor
            if mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]:
                return list_of_integers[mid]
            else:
                right = mid - 1
        else:
            left = mid + 1

    # Return the last element if it's a peak
    return list_of_integers[left]

# Test the function
print(find_peak([1, 2, 3, 1]))  # Output: 3

