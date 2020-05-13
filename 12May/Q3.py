# count of columns having odd number of 1s
def col_having_odd_ones(ls, n, m):
    count = 0
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += ls[i][j]
        if sum % 2 == 1:
            count += 1
    return count


ls = []
n = int(input("Enter row size:"))
m = int(input("Enter column size:"))
for i in range(n):
    temp = []
    print("Enter row ", i+1)
    for j in range(m):
        temp.append(int(input()))
    ls.append(temp)
print("Output : ", col_having_odd_ones(ls, n, m))