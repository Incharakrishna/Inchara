def sum(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
num_list = [50,30,40,60]

sum_list =sum(num_list)
print("sum of values in list is : " +str(sum_list))
