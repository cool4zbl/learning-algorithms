class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
            Constructs a differential array solution with time complexity O(1)
            diff[0] = arr[0]             # i = 0
            dff[i]  = arr[i] - arr[i-1]  # i >= 1

            Conctructs the original array through the differential array.
            arr[0] = diff[0]             # i = 0
            arr[i] = diff[i] + arr[i-1]  # i >= 1

            if we want to add `x` to interval arr[i...j],
            then we add diff[i] with x, diff[i] += x,
            and we substract diff[j+1] with x, diff[j+1] -= x,
            then we re-construct the original array through diff array,
            the interval arr[i...j] values are changed by `x`

            since the original array is N zeros, we just need one array here.
        """

        diff =[0] * n

        for first, last, seats  in bookings:
            diff[first - 1] += seats
            # Note the `last` value here
            if last < len(diff):
                diff[last] -= seats

        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff

s = Solution()
arr =[[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(s.corpFlightBookings(arr, n))
arr = [[3,3,5],[1,3,20],[1,2,15]]
n = 3
print(s.corpFlightBookings(arr, n))