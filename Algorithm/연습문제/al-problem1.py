def sum(i):

   global result
   n=0
   result= 0
   while (n<=i):
     result += n
     n = n+1
   print(result)

sum(100)