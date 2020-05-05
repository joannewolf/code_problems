# 1. How should we move low and high?
# 2. How should we compute mid?
# 3. What would be the condition in while loop?

# return exact index of target, else -1
def binary_search(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        # mid = (L + R) / 2 # mostly same as below, only give wrong mid when L < 0, R < 0, (L + R) % 2 = 1
        mid = L + (R - L) // 2 # give the lower mid when #elements is even
        # mid2 = L + (R - L + 1) // 2 # give the higher mid when #elements is even
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return -1

# return maximum element index which <= target if it exists
def binary_search2(array, target):
    L = 0
    R = len(array) - 1
    while L < R:
        mid = L + (R - L + 1) // 2 # use higher mid when #elements is even, using lower mid will result in infinite loop
        if array[mid] == target:
            return mid
        if array[mid] <= target:
            L = mid # because mid might be the answer
        else:
            R = mid - 1
    # stop when L == R and return 
    return L

# return maximum element index which <= target, duplicate elements not allowed
def binary_search3(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        mid = (L + R) // 2
        if array[mid] <= target:
            L = mid + 1
        else:
            R = mid - 1
    return R

# return minimum element index which > target, duplicate elements allowed
def binary_search4(array, target):
    L = 0
    R = len(array) - 1
    ans = -1
    while L <= R:
        mid = (L + R) // 2
        if array[mid] <= target:
            L = mid + 1
        else:
            ans = mid # mid is last possible answer
            R = mid - 1
    return ans
    # return L
    # return R + 1

# return minimum element index which > target if exists, duplicate elements allowed
def binary_search5(array, target):
    L = 0
    R = len(array)
    while L < R:
        mid = (L + R) // 2
        if array[mid] <= target:
            L = mid + 1
        else:
            R = mid
    return L

# return minimum element in sorted, rotated array, duplicate elements allowed
def binary_search6(array):
    L = 0
    R = len(array) - 1
    while L < R:
        mid = (L + R) // 2
        if array[mid] == array[R]:
            R -= 1
        elif array[mid] > array[R]:
            L = mid + 1
        else:
            R = mid
    return R

def binary_search6_recursion(array, L, R):
    if R < L:
        return 0
    if L == R:
        return L
    mid = (L + R) / 2
    if mid < R and array[mid + 1] < array[mid]:
        return mid + 1
    if mid > L and array[mid] < array[mid - 1]:
        return mid
    if array[mid] < array[R]:
        return binary_search6_recursion(array, L, mid - 1)
    else:
        return binary_search6_recursion(array, mid + 1, R)


array = [ 2, 3, 4, 10, 40 ]
duplicate_array = [ 2, 2, 3, 4, 10, 10, 10, 20, 40 ]
target = 3
# print binary_search5(duplicate_array, target)

rotated_array = [3, 4, 10, 40, 2]
rotated_duplicate_array = [2, 3, 3, 4, 10, 10, 40, 2, 2] 
# print binary_search6(rotated_array)
# print binary_search6_recursion(rotated_array, 0, len(rotated_array) - 1)
# print binary_search6_recursion(rotated_duplicate_array, 0, len(rotated_duplicate_array) - 1)
