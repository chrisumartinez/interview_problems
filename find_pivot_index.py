""" 
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
The array will not contain duplicates.

Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].

Hints on the original problem: https://www.interviewbit.com/problems/rotated-array/ """

#Binary Search Method:
def find_pivot_index(input_list):
  low = 0
  high = len(input_list) - 1
  min_index = 0 

  while low < high-1:
    if high - low % 2 == 0:
      pivot = int((high - low) / 2) + low
    else:
      pivot = int((high - low + 1) / 2) + low

    if input_list[pivot] < input_list[min_index]:
      high = pivot
      min_index = pivot
    else:
      low = pivot
  return min_index

# Brute Force Method:
# def find_pivot_index(input_list):
#     # List is sorted, but then rotated.
#   # Find the minimum element in less than linear time
#   # return it's index
#     for index in range(0, len(input_list)):
#       # if current element index is larger than previous elem,
#       if input_list[index] < input_list[index - 1]:
#           return index
#     return 0

list = [7,8,9,10,11,12,0,1,2,3,4,5,6]
print(find_pivot_index(list))





# while current element is larger then tha previous element
#check the next element
# otherwise, that element is the minimum element
# return the min