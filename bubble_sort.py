""" 
Given an unsorted list of integers, sort those integers using the Bubble Sort algorithm. Return the number of swaps required to sort the list.

Bubble Sort is a simple sorting algorithm that works as follows:
1. Start at the beginning of the list, and traverse through each element.
2. For each element, if the element is larger than the one that comes after it, swap them.
3. Once you reach the end of the list, if you have not made any swaps, you are done, and the list is sorted.
4. Otherwise, go back to step 1.

Given a list of numbers to sort, return the count of swaps you must make when using the Bubble Sort Algorithm that will result in a sorted list.

Example:

[6, 2, 4, 3]
[2, 6, 4, 3]; swap 6 with 2
[2, 4, 6, 3]; swap 6 with 4
[2, 4, 3, 6]; swap 6 with 3. End of the list has been reached, go back to the beginning.
[2, 3, 4, 6]; swap 4 with 3

Done! Total swaps: 4. """
def bubble_sort_swaps(nums):
  overall_swaps = 0
  swap_flag = True
  swap_counter = 0
  while swap_flag:
    for index in range(0, len(nums)-1):
      if nums[index] > nums[index+1]:
        #swap
        nums[index] ^= nums[index+1]
        nums[index+1] ^= nums[index]
        nums[index] ^= nums[index+1]

        swap_counter += 1
    #print("Swap Counter after each iteration: ", swap_counter)
      # no swaps, then list is sorted:
    if swap_counter == 0:
      swap_flag = False
    else:
      # dump swap_counter into overall_swaps, reset swap_counter = 0
      overall_swaps += swap_counter
      swap_counter = 0

  return overall_swaps

nums = [6, 2, 4, 3]
print(bubble_sort_swaps(nums))