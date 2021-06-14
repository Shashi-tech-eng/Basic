num=int(input())
check=num%2
if check==0:
    print("even")
else:
    fact = 1
  
    for i in range(1,num+1):
       fact = fact * i
    print (fact)
