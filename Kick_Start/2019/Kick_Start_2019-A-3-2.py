# Contention
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/0000000000069881
# O(Q^2logN)
# Ref:
# https://www.shuzhiduo.com/A/kPzO40AaJx/
# https://github.com/zouzhitao/competitive-programing/blob/master/kick-start/2019-roundA-contention.cpp

# For given k, check if we can find a booking order achieving it
def check(k):
    available_l = [0] * Q
    for i, (l, r) in enumerate(bookings):
        available_l[i] = max(available_l[i], l) # The left point that interval i can start book
        available_after = r
        count = 0
        # Check if we can find k seats for booking i
        for j in range(i + 1, Q):
            (l2, r2) = bookings[j]
            if l2 >= r: # Interval j is fully after i, won't affect i's seats
                break
            if r2 <= r:
            # Interval j is fully wrapped by i, j has to be handled before i, otherwise it will get no seats
            # In other words, interval i cannot get the seats in interval j
                if available_l[i] < l2:
                    count += (l2 - available_l[i])
                available_l[i] = max(available_l[i], r2)
                if count >= k: # Interval i can get k seats, leave the remaining seats to other interval
                    available_after = l2 - (count - k)
                    break
        if count < k:
            count += (r - available_l[i])
            if count < k: # Even getting all possible seats, interval i still cannot get k seats
                return False
            available_after = r - (count - k)

        # For all the intervals after i and their left point < available_after, they have to be handled after i otherwise interval i cannot get k seats
        for j in range(i + 1, Q):
            (l2, r2) = bookings[j]
            if l2 >= available_after: # Interval j can be handled before i
                break
            if r < r2: # Interval j has to be handled after i, but is not fully wrapped by i, 
                available_l[j] = max(available_l[j], r)
    return True

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    bookings = []
    max_request = 0
    for i in range(Q):
        [l, r] = [int(n) for n in input().split()]
        max_request = max(max_request, r - l + 1)
        # l - 1 make seats as 0-based and left-closed-right-open interval
        # -r make sorting descending
        bookings.append((l - 1, -r))
    bookings.sort() # Sort bookings by left point ascending, then right point descending
    # i.e. if interval i < j, then it must be either li..lj..ri..rj or li..lj..rj..ri or li=lj..rj..ri
    # If interval j is fully wrapped by i, j will be behind i
    for i in range(Q):
        bookings[i] = (bookings[i][0], -bookings[i][1])

    # Use binary search to find the max k which can be achieved
    l, r = 0, max_request
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if check(mid):
            ans = mid
            l = mid + 1 # keep search [mid + 1, r] for more left target
        else:
            r = mid - 1
    
    print(f"Case #{t + 1}: {ans}")
