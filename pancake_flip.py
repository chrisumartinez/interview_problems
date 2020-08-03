""" 
Sort a list of integers, using only "pancake flips". A pancake flip is defined as taking the first k elements 
of a list and reversing them. Your function should return a list of integers, containing the k-values for each flip. 
So long as the series of flips you return creates a sorted list, the answer is correct.

Example:
[5, 2, 3, 4, 1]; Starting array
[1, 4, 3, 2, 5]; Reverse first 5 integers, k=5
[4, 1, 3, 2, 5]; Reverse first 2 integers, k=2
[2, 3, 1, 4, 5]; Reverse first 4 integers, k=4
[3, 2, 1, 4, 5]; Reverse first 2 integers, k=2
[1, 2, 3, 4, 5]; Reverse first 3 integers, k=3


[2, 5, 7, 1, 3, 9]: Starting Array
[2, 5, 7, 1, 3, 9]: Reverse 0 integers, k=0
[7, 5, 2, 1, 3, 9]: Reverse 3 integers, k = 3
[3, 1, 2, 5, 7, 9]: reverse 5 integers, k = 5
[5, 2, 1, 3, 7, 9]: reverse 4 integers, k = 4
[3, 1, 2, 5, 7, 9]: reverse 4 integers, k = 4
[2, 1, 3, 5, 7, 9]: reverse 3 integers, k = 3
[1, 2, 3, 5, 7, 9]: reverse 2 integers, k = 2

k values: [0,3,5,4,4,3,2]

Sorted!
k-values are: [5, 2, 4, 2, 3] """


# reverses the first k elements of an array
def flip(arr, k):
  for i in range(k//2):
    arr[i], arr[k-i-1] = arr[k-i-1], arr[i]

def getMaxIndex(nums, array_size):
  max = 0
  for index in range(0, array_size):
    if nums[index] > nums[max]:
      max = index
  return max

def pancake_sort(nums):

  array_size = len(nums)
  k_list = []

  while array_size > 1:
    print("Array: ", nums)
    #get the max:
    index = getMaxIndex(nums, array_size)
    #print("Max Index: ", index)
    
    # if the index of the max element is not equal to the end, then
    # move it to the end by flipping it
    if index != array_size:
      #move the max number to the very beginning:
      if index != 0:     
        flip(nums, index+1)
        k_list.append(index+1)
        #print("Flipping the first ", index + 1, "integers")

      #print("Flipped Number to Move Max to the Beginning Index: ", nums)

      #then flip the array:
      flip(nums, array_size)
      k_list.append(array_size)
      #print("Flipping the first ", array_size, "integers")
      #print("")
    #decrement our array_size by 1, showing that the max element is in its correct spot:
    array_size -= 1

  print("Final Sorted Array: ", nums)
  return k_list

nums = [5, 2, 3, 4, 1]
nums2 = [2, 5, 7, 1, 3, 9]
# nums2 = [5, 2, 3, 4, 1]
print(pancake_sort(nums))
print(pancake_sort(nums2))