print("Which method do you want to use?: ")
print("1.With an auxiliar variable 2.With successive decreases")

option = input("Type 1 or 2: ")

# getting the user option
while option != "1" and option != "2":
    option = input("Wrong! Type 1 or 2: ")

a = input("a: ")
# if a is not a number show a loop while the user enters a number
while not a.isnumeric():
    a = input("a (numeric value): ")

b = input("b: ")
# if b is not a number show a loop while the user enters a number
while not b.isnumeric():
    b = input("b (numeric value): ")

# make the values integers
a = int(a)
b = int(b)

if option == "1":
    # exchange the values with an auxiliar variable aux
    aux = a
    a = b
    b = aux
elif option == "2":
    # successive decreases e.g: a = 2, b = 4; a = 2 - 4 = -2; b = -2 + 4 = 2; a = 2 - (-2) = 4
    a = a - b
    b = a + b
    a = b - a

# print the results
print("a: " + str(a) + " / b:" + str(b))