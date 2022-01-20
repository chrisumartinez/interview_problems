""" 
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated
 and only the integer part of the result is returned.

Do not use any built square root functions.

Example 1:
Input: 4
Output: 2


Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned. """

def squareRoot(num):
    # low = 0, high = num:
    # remove base cases:
    if num < 2:
        return num
    low = 1
    high = num

    while low <= high:
        mid = low + (high-low) // 2

        print("Low: ", low, "Mid: ", mid, "High: ", high)
        print("Mid * Mid: " , mid * mid)
        #perfect base
        if mid * mid == num:
            return mid
        if mid * mid > num:
            high = mid - 1
        else:
            low = mid + 1
    #return floor
    return high

sampleInput = 125
print(squareRoot(sampleInput))