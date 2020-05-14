# Count of path in a grid
def count_path_of_grid(m):
    ls = []
    for i in range(m):
        temp = []
        for j in range(m):
            temp.append(0)
        ls.append(temp)
    for i in range(m):
        for j in range(m):
            ls[i][0] = 1
            if i >= j:
                ls[i][j] = ls[i-1][j] + ls[i][j-1]
            else:
                break
    return ls[-1][-1]


n = int(input("Enter array size:"))
print(count_path_of_grid(n) % (10 ^ 9 + 7))