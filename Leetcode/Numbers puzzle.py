from itertools import permutations
penalty=[]
def findpenalty(li):
    #19N81A04C3
    sum=0
    for i in range(len(li)-1):
        sum+=abs(li[i+1]-li[i])
    return sum

n=int(input())
arr=list(map(int,input().split()))[:n]
perm=permutations(arr,3)
for i in list(perm):
    list_i=list(i)
    penalty.append(findpenalty(list_i))
print(min(penalty))
    
