def lower_num(num1, num2):
    
    if num1 <= num2 :
        lowest = num1
    
    else :
        lowest = num2
    
    return lowest    


first_num = int(input("introduce el primer numero: "))
second_num = int(input("introduce el segundo numero: "))
print("el mas pequeño es " + str(lower_num(first_num, second_num)))


