def add (x, y):
    return x + y

def sub (x, y):
    return x - y

def mul (x, y):
    return x * y

def div (x, y):
    return x / y

def power (x, y):
    return x ** y

user1 = int(input("enter your first number "))
user2 = int(input("enter your second number "))

print ("you're options are:")
print ("a if you want to add ")
print ("b if you want to subtract ")
print ("c if you want to multiply ")
print ("d if you want to divide ")
print ("e if you want to square ")

ans = input()

if ans == "a":
    print(user1, "+", user2, "=", add(user1, user2))

elif ans == "b":
    print(user1,"-", user2, "=", sub(user1, user2))

elif ans == "c":
    print(user1,"*", user2, "=", mul (user1, user2))

elif ans == "d":
    print(user1,"/", user2, "=", div (user1, user2))

elif ans == "e":
    print(user1,"**", user2, "=", power (user1, user2))


    



