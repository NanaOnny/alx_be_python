pattern = int(input("Enter the size of the pattern:"))

i = 1
while i <= pattern:
    print("*", end="")
    i = i + 1
    for j in range(pattern):
        print("*", end="")

    print()



