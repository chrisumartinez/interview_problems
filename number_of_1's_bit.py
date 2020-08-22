""" 
Given an integer value in Python, return the count of "1" bits the number has, 
when converted as a 32-bit unsigned integer.

For example:


1:    00000000000000000000000000000001 # return 1
2:    00000000000000000000000000000010 # return 1
3:    00000000000000000000000000000011 # return 2
4:    00000000000000000000000000000100 # return 1
5:    00000000000000000000000000000101 # return 2
100 : 00000000000000000000000000100100 # return 2
500:  00000000000000000000000111110100 # return 6 """


def count_set_bits(num):
    # #convert into a 32 bit signed integer:


    counter = 0
    while num > 0:
        num &= num -1
        counter += 1

    # #initiate values:
    # bit = {}
    # bit[0] = 0
    # bit[1] = 0

    # #begin dividing: 32 times down to 0
    # while num != 0:
    #     print("Num: ", num)
    #     #check for a remainder:
    #     if num % 2 == 0:
    #         #if its zero, append a zero:
    #         bit[0] += 1
    #         num //= 2
    #     else:
    #         #append a 1:
    #         bit[1] += 1
    #         #then we do integer division
    #         num //= 2
    # #now return # of 1's:
    return counter


print(count_set_bits(200))