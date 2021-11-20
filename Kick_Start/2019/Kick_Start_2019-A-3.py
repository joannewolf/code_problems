# Contention
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050e01/0000000000069881
# O(Q^3), TLE on test set 2

T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    bookings = []
    for i in range(Q):
        [l, r] = [int(n) for n in input().split()]
        # l - 1 make seats as 0-based and left-closed-right-open interval
        # -r make sorting descending
        bookings.append((l - 1, -r))
    bookings.sort() # Sort bookings by left point ascending, then right point descending
    # i.e. if interval i < j, then it must be either li..lj..ri..rj or li..lj..rj..ri or li=lj..rj..ri
    # If interval j is fully wrapped by i, j will be behind i
    for i in range(Q):
        bookings[i] = (bookings[i][0], -bookings[i][1])

    # The seats that last booking can get doesn't depend on its previous booking order
    # For each iteration, from the remaining booking set, consider each booking as the last booking and greedily choose the one which has the most available seats
    # In other words, we'll decide the booking order backwardly and find the min booked seats across Q iterations
    ans = N + 1
    while bookings and ans != 0:
        max_seats = 0
        index = -1 # The index of booking which has max available seats

        flag = 0 # The last ending point of previous interval
        for i, (l, r) in enumerate(bookings):
            seat = 0
            if r <= flag: # Interval i is fully wrapped by previous interval, it can get no seats
                continue
            if flag < l:
                flag = l

            # For the intervals after interval i, find how many seats are remaining for interval i after they booked
            flag2 = flag
            for j in range(i + 1, len(bookings)):
                (l2, r2) = bookings[j]
                if flag2 >= r or l2 >= r: # Interval j is fully after interval i
                    break
                if r2 <= flag2: # Interval j is fully wrapped by previous interval, it won't affect interval i
                    continue
                if flag2 < l2:
                    seat += (l2 - flag2)
                flag2 = r2
            if flag2 < r:
                seat += (r - flag2)

            flag = max(flag, r)
            if seat > max_seats:
                max_seats = seat
                index = i

        del bookings[index]
        ans = min(ans, max_seats)
    
    print(f"Case #{t + 1}: {ans}")
