#Square root of a number:
def square_root(n):
     temp = 0
     while True:
           if temp * temp<= n:
               temp += 1
           else:
               temp -= 1
               break
     return temp




a = int(input("Enter a number:"))
print("Square root of ",a,"is:",square_root(a))