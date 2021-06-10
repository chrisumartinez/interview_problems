def addDigits(num):
    str_digit_count = len(str(num))
    # condition for one digit number:
    while str_digit_count > 1:
        str_num = str(num)
        num = 0
        for digit in str_num:
            num += int(digit)
        str_digit_count = len(str(num))

    return num


num = 38
num2 = 0
print(addDigits(num))  # Expected 2
print(addDigits(num2))  # Expected 0
