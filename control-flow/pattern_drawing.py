size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("input a positive number")
else:
    row = 0
while row <size:
    for x in range(size):
        print("*" , end="")
print()
row =+ 1
