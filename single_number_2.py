""" 
Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example:
>> arr = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
>> single_number(arr) # returns 4

OG Platform:  https://www.interviewbit.com/problems/single-number-ii/  """

def single_number(nums):
    single_number_list = []
    #Double For Loop:
    for bit in range(0, 31):
        num_of_bits_counter = 0
        for num in nums:
            #Count the #'s of 1's in the nth position:
            #mask is whatever we are at in bit:
            mask =  1 << bit
            if (mask&num) == mask:
                #if we have a matching number bit:
                num_of_bits_counter += 1
        #we check if # of nth bits is a multiple of 3:
        if num_of_bits_counter % 3 == 0:
            #append a 0:
            single_number_list.append(0)
        else:
            single_number_list.append(1)
    
    

    #reverse the list:
    single_number_list = single_number_list[::-1]

    #print list:
    print(single_number_list)

    #build the number using multiplication:
    output = 0
    for bit in single_number_list:
        output = (output << 1) | bit
        print(output)

    return output


arr = [1, 1, 1, 3, 3, 3, 4]
print(single_number(arr)) #Expected: 4
