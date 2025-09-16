def highest_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        highest_num = num1
    elif num2 >= num1 and num2 >= num3:
        highest_num = num2
    else:
        highest_num = num3
    return highest_num
    
    
first_num = int("indroduce el primer numero: "))
second_num = int("introduce el segundo numero: "))
third_num = int("introduce el tercer numero: "))


print("El número más alto es:", highest_num(first_num, second_num, third_num))
