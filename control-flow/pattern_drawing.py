pattern_number = int(input("Enter the size of the pattern: "))

num = 0
while num < pattern_number:
    inner = 0
    while inner < pattern_number:
        print("*", end="")
        inner += 1
    print()
    num += 1