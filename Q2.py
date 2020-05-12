#Maximumheight staircase
def max_height_staircase(n):
   temp= 0
   while True:
       if temp +1 < n:
           temp += 1
           n= n- temp+1
       else:
          break
   return temp

a =  int(input("Enter number of square blocks:"))
print("Maximum height of staircase:",max_height_staircase(a))