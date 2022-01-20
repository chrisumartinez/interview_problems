""" 
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is no future day 
for which this is possible, put 0 instead.

Input
The length of temperatures will be in the range [1, 30000]. Each temperature 
will be an integer in the range [30, 100].

Sample
Input#1
T = [73, 74, 75, 71, 69, 72, 76, 73]
Output#1
[1, 1, 4, 2, 1, 1, 0, 0] """

def dailyTemperatures(dailyTemps):
    warmer_temp_days = []
    i = 0
    counter = 0
    #while we iterate through dailyTemps
    while i < len(dailyTemps):
        #pop the first item in the list, store it into cur_temp
        cur_temp = dailyTemps.pop(i)
        
        #Compare cur_temp with each temperature in dailyTemp
        for temp in dailyTemps:
            #Keep Track of a days_counter:
            counter += 1
            #if the temperature is hotter than the current temp:
            if temp > cur_temp:
                #append the days_counter to our result
                warmer_temp_days.append(counter)
                #reset the counter
                counter = 0
                #break through the loop, were done iterating
                break
            # Reach end of the array
            elif counter == len(dailyTemps):
                #no hotter day, then we append a 0
                warmer_temp_days.append(0)
                #reset the counter
                counter = 0
    #append the index at end of the array
    warmer_temp_days.append(0)
    return warmer_temp_days

sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))

""" 


73 -> 74
if dailytemp[index] > stack[-1]:
    # while through the length of the stack:
        if dailytemp[index] > dailyTemp[element of the stack]:
            append the index - element of the stack
        else:
            push it into the stack




    # #Initiate all values to 0:
    # # for elem in dailyTemps:
    # #     warmer_temp_days.append(0)
    # #base case
    # stack.append(0)
    # stack_val.append(dailyTemps[0])
    # temp = []

    # for index in range(1, len(dailyTemps)):
    #     #if theres a stack and cur_val > top of the stack
    #     if stack and dailyTemps[index] > dailyTemps[stack[-1]]:
            
    #         # #Iterate until either the stack is empty or if the element in the stack is bigger than dailyTemps[index]
    #         if dailyTemps[index] > dailyTemps[stack[0]]:
    #             while stack and dailyTemps[index] > dailyTemps[stack[-1]]:
    #                 #warmer_temp_days.append(index - stack[-1])
    #                 temp.append(index - stack[-1])
    #                 stack.pop()
    #                 stack_val.pop()
    #             stack.append(index)
    #             stack_val.append(dailyTemps[index])
    #         else:
    #             stack.append(index)
    #             stack_val.append(dailyTemps[index])
    #     else:
    #         # then if either theres a smaller # of if the stack is empty, then we push it the index into the stack
    #         # and append a 0 into the warmer_days_list
    #         stack.append(index)
    #         stack_val.append(dailyTemps[index])
    #     if len(stack) == 1:
    #         print("Temp: ", temp)
    #         temp = temp[::-1]
    #         warmer_temp_days.extend(temp)
    #         temp = []
    #     print("Stack: ", stack)
    #     print("Stack_val After Code: ", stack_val)
    #     print("Warmer Days Array: ", warmer_temp_days)
    #     print()
    
    # # if theres anything left in the stack, then we append 0 for how many elems in stack:
    # for elem in stack:
    #     warmer_temp_days.append(0)
            



         # #If its a greater temp, and theres a stack
        # print("Comparing Top of Stack: ", dailyTemps[stack[-1]] , " and Current Value: ", dailyTemps[index])
        # if stack and dailyTemps[index] > dailyTemps[stack[-1]]:
        #     warmer_temp_days.append(len(stack))
        #     while stack:
        #         if dailyTemps[index] > dailyTemps[stack[-1]]:
        #             warmer_temp_days.append(len(stack))
        #             stack.pop()
        #         else:
        #             break
        # else:
        #     #if its smaller, than we append it to the stack
        #     stack.append(dailyTemps[index])






            # for index in  range(0, len(dailyTemps)):
    #     days_counter = 1
    #     for checked_temp in dailyTemps[index+1:]:
    #         if checked_temp > dailyTemps[index]:
    #             warmer_temp_days.append(days_counter)
    #             break
    #         else:
    #             days_counter += 1

"""