i = 1  # Rows
j = 0  # Columns
n = 5
while i <= n:
    while j <= i - 1:
        print("*", end="")
        j += 1
    print("\r")
    i += 1
    j = 0
