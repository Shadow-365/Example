#Asterisk in Python
n=int(input("Enter the number of asterisk :"))
print("The asterisk is given below :")

for i in range(n):
    for j in range(i):
        print("*", end="")
    print()