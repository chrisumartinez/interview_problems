""" 
You work at a sorting factory. You sort things. One day, your boss comes in to tell you there's a new ball shipment. There are three kinds of balls: 
red, white, and blue. You've been charged with the task of sorting these balls. Unfortunately, your boss won't let you take your lunch break until 
you've finished sorting the balls, so you want to do it quickly.

Instructions:
Create an algorithm that will sort an array of n elements, each element either red, white or blue. The integers 0, 1, 2, will represent red, white,
and blue, respectively. Perform this sorting in-place, using constant space. Your solution should complete this 
in O(n) time, any longer and you'll miss your lunch break!

Example:
[0, 1, 0, 1, 2, 1] --> [0, 0, 1, 1, 2]

Extra Challenge:
The boss is threatening to replace your job with a very efficient sorting robot, provided you don't perform better than it would. Luckily for you, 
the robot requires taking two passes over the array to sort the elements. You're not sure, but you think there might be a way to sort the elements that 
requires taking only one pass over the array, thus handily out-performing the robot.
 """

def color_sort(nums):

    if len(nums) == 1:
        return

    high = len(nums) - 1
    low = 0
    index = 0

    while index <= high:

        print(nums)
        #if num = 0
        if nums[index] == 0:

            #swap
            temp = nums[low]
            nums[low] = nums[index]
            nums[index] = temp


            #increase our low bound:
            low += 1

        if nums[index] == 2:

            #swap
            temp = nums[high]
            nums[high] = nums[index]
            nums[index] = temp

            #decrement our high bound:
            high -= 1

            #decrement the counter:
            index -= 1

        #increment our index iterator:
        index += 1

    return nums

arr = [1,1,0,0,2,1,1,1,0,2,0]
arr2 = [2,2,1]
print(color_sort(arr))



  # Loop over the list,
  # if you see a 1, leave it alone

