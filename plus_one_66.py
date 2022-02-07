def plusOne(digits):
    # recursive function:
    nums_str = ""
    result = []
    for digit in digits:
        nums_str += str(digit)
    nums = str(int(nums_str) + 1)
    for num in nums:
        result.append(num)
    return result


digits = [1, 2, 3]
print(plusOne(digits))  # expected , [1,2,4]
digits2 = [9, 9]
print(plusOne(digits2))  # expected, [1,0]
