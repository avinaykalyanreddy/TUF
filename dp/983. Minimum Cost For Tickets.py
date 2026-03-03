"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.


"""

days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]


def find_day(val):
    low = 0
    high = len(days) - 1

    while low <= high:

        mid = (low + high) // 2

        if days[mid] == val:

            return days[mid]


        elif days[mid] > val:

            high = mid - 1

        else:

            low = mid + 1

    return days[low]


seen = {}


def recursion(day):
    if day > days[-1]:
        return 0

    present_day = find_day(day)

    if present_day in seen:
        return seen[present_day]
    ans = float("inf")
    for i in range(len(costs)):

        if i == 0:

            ans = min(costs[i] + recursion(present_day + 1), ans)

        elif i == 1:

            ans = min(costs[i] + recursion(present_day + 7), ans)

        else:

            ans = min(costs[i] + recursion(present_day + 30), ans)

    seen[present_day] = ans
    return seen[present_day]


print(recursion(days[0]))