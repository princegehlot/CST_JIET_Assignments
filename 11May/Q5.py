def min_xor(temp):
    min = temp[0] ^ temp[1]
    m = 0
    n = 1
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if min > temp[i] ^ temp[j]:
                min = temp[i] ^ temp[j]
                m = i
                n = j
    print("Min X-OR Value: ", min, " of ", temp[m], " and ", temp[n])


print("First Part:")
ls = []
n = int(input("Enter size of array:"))
print("Enter ", n, " elements:")
for i in range(n):
    ls.append(int(input()))
min_xor(ls)