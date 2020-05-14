def linear_search(ls, x):
    i = 0
    j = len(ls)-1
    while i <= len(ls)-1 and j >= 0:
        if ls[i][j] == x:
            print("Found at (", i, ",", j, ")")
            return
        elif ls[i][j] > x:
            j -= 1
        else:
            i += 1
    print("Element not found")
    return


ls = []
n = int(input("Enter size:"))
for i in range(n):
    temp = []
    print("Enter row ", i+1)
    for j in range(n):
        temp.append(int(input()))
    ls.append(temp)
x = int(input("Enter element to be searched:"))
linear_search(ls, x)
