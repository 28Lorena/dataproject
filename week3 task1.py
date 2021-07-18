my_file = open ("number.txt", "w")

my_file.close()


per1 = "3\n"
per2 = "45\n"
per3 = "83\n"
per4 = "21\n"

my_file = open ("number.txt.", "a")

my_file.write (per1)
my_file.write (per2)
my_file.write (per3)
my_file.write (per4)

my_file.close()

my_file = open ("number.txt.", "r")

data = my_file.read().replace ("\n", ",")

my_file.close()

print (data)


