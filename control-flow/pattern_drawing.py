size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
    for col in range(size):
        print("*", end="")  # print a row of stars
    print()  # move to the next line
    row += 1  # increase row count AFTER printing a row
