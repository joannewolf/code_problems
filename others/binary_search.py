# 1. How should we move low and high?
# 2. How should we compute mid?
# 3. What would be the condition in while loop?

# return index of target, not allow duplicate
# if target not in array, the final L is the index for inserting
def binary_search(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        # mid = (L + R) / 2 # mostly same as below, only give wrong mid when L < 0, R < 0, (L + R) overflow
        mid = L + (R - L) // 2 # give the lower mid when #elements is even
        # mid2 = L + (R - L + 1) // 2 # give the higher mid when #elements is even
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    print("L", L, "R", R)
    # return L
    return -1

# return first index of target, allow duplicate
# if target not in array, the final L is the index for inserting
def binary_search2(array, target):
    ans = -1
    L = 0
    R = len(array) - 1
    while L <= R:
        # mid = L + (R - L) // 2
        mid = L + (R - L + 1) // 2
        if array[mid] < target:
            L = mid + 1
        elif array[mid] > target:
            R = mid - 1
        else:
            ans = mid
            R = mid - 1 # keep search [L, mid - 1] for more left target

    print("L", L, "R", R)
    return ans

# return last index of target, allow duplicate
# if target not in array, the final L is the index for inserting
def binary_search3(array, target):
    ans = -1
    L = 0
    R = len(array) - 1
    while L <= R:
        # mid = L + (R - L) // 2
        mid = L + (R - L + 1) // 2
        if array[mid] < target:
            L = mid + 1
        elif array[mid] > target:
            R = mid - 1
        else:
            ans = mid
            L = mid + 1 # keep search [mid + 1, R] for more right target

    print("L", L, "R", R)
    return ans

# final R is max element index which <= target, allow duplicate
# final L is min element index which > target
def binary_search4(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        mid = (L + R) // 2
        if array[mid] <= target:
            L = mid + 1
        else:
            R = mid - 1
    print("L", L, "R", R)
    return R

# final R is max element index which < target, allow duplicate
# final L is min element index which >= target
def binary_search5(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        mid = (L + R) // 2
        if array[mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    print("L", L, "R", R)
    return R

# return first minimum element in sorted, rotated array, allow duplicate
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
    mid = (L + R) // 2
    if mid < R and array[mid + 1] < array[mid]:
        return mid + 1
    if mid > L and array[mid] < array[mid - 1]:
        return mid
    if array[mid] < array[R]:
        return binary_search6_recursion(array, L, mid - 1)
    else:
        return binary_search6_recursion(array, mid + 1, R)

# when feeding array element to function will return [False, False, ..., True, True]
# return first element that function return True
def func(num, target):
    return num >= target
def binary_search7(array, target):
    L = 0
    R = len(array) - 1
    ans = -1
    while L <= R:
        mid = (L + R) // 2
        if func(array[mid], target):
            ans = mid
            R = mid - 1 # keep search [L, mid - 1] for more left target
        else:
            L = mid + 1
    print("L", L, "R", R)
    return ans

array = [ 2, 4 ]
# array = [ 2, 3, 4, 10, 40 ]
duplicate_array = [ 2, 2, 2, 3, 4, 4, 4, 10, 10, 10, 10, 10, 20, 40 ]
# print(binary_search5(duplicate_array, 0))
# print(binary_search5(duplicate_array, 2))
# print(binary_search5(duplicate_array, 3))
# print(binary_search5(duplicate_array, 7))
# print(binary_search5(duplicate_array, 10))
# print(binary_search5(duplicate_array, 40))
# print(binary_search5(duplicate_array, 50))
print(binary_search7(array, 2))

rotated_array = [3, 4, 10, 40, 2]
rotated_duplicate_array = [2, 3, 3, 4, 10, 10, 40, 2, 2] 
# print(binary_search6(rotated_duplicate_array))
# print(binary_search6_recursion(rotated_array, 0, len(rotated_array) - 1))
# print(binary_search6_recursion(rotated_duplicate_array, 0, len(rotated_duplicate_array) - 1))

def ternary_search(array, target):
    L = 0
    R = len(array) - 1
    while L <= R:
        mid1 = L + (R-L) // 3
        mid2 = R - (R-L) // 3
        if array[mid1] == target:
            return mid1
        if array[mid2] == target:
            return mid2

        if target < array[mid1]: # target lies between l and mid1
            R = mid1 - 1
        elif target > array[mid2]: # target lies between mid2 and r
            L = mid2 + 1
        else: # target lies between mid1 and mid2
            L = mid1 + 1
            R = mid2 - 1
