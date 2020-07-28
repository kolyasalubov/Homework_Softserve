number= input("Enter number:")

print(int(number[0])*int(number[1])*int(number[2])*int(number[3]))
list = [int(number[0]),int(number[1]),int(number[2]),int(number[3])]
print(list)
list.sort()
print(list)

#обернене число
number_1="".join(list.reverse) замість 5, 6 та 7 стрічки
print("Reverse number is: ", number_1)

# Добуток цифр числа без циклу
number = int (input ("Введіть чотирьохзначне число: "))
d1 = number % 10
number = number // 10
d2 = number % 10
number = number // 10
d3 = number % 10
number = number // 10

print("Добуток цифр числа:", number * d1 * d2 * d3)
