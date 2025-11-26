def calculate_average(numbers):
    try:
        total=0
        for i in range(len(numbers)):
            total += numbers[i]
        return total/len(numbers)
    except ZeroDivisionError:
        print("Division by zero")
        return 0

def get_list_elements(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print("Index out of range")


data1 = [10,20,30,40,50]
data2 = [5,15]
data3 = []

print("Average of data1:",calculate_average(data1))
print("Average of data2:",calculate_average(data2))
print("Average of data3:",calculate_average(data3))

my_list = [10,20,50]
print(get_list_elements(my_list, 1))
print(get_list_elements(my_list, 5))
print(get_list_elements("not_a_list", 0))
