num1 = int(input("enter your first number "))
num2 = int(input("enter your second number "))

print ("enter a if you want to add num 1 and num 2")
print ("enter b if you want to subtract num 1 from num 2")
print ("enter c if you want to multiply num 1 and num 2")
print ("enter d if you want to divide num 1 from num 2")
print ("enter e if you want to square num 1 and num 2")

ans = input()

if ans == "a":
    add = num1 + num2
    print(num1, "+", num2, "=", add)

elif ans == "b":
    sub = num1 - num2
    print(num1,"-", num2, "=", sub)

elif ans == "c":
    mul = num1 * num2
    print(num1,"*", num2, "=", mul)

elif ans == "d":
    div = num1 / num2
    print(num1,"/", num2, "=", div)

elif ans == "e":
    power = num1 ** num2
    print(num1,"**", num2, "=", power)
