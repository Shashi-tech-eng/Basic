n=int(input())
count=0
def checkZ(x):
    a=str(x)
    check=0
    list_a=list(a)
    if len(a)==1:
        return True
    if len(list_a) != len(set(list_a)):
        return True
    elif len(a)>1:
        for i in range(len(list_a)-1):
            if i%2==0:
                if int(a[i])<int(a[i+1]):
                    check=1
                else:
                    check=0
            elif i%2==1:
                if int(a[i])>int(a[i+1]):
                    check=1
    if check==1:
        return True
    else:
        return False

for i in range(n+1):
    if checkZ(i):
        count+=1
print(count)
