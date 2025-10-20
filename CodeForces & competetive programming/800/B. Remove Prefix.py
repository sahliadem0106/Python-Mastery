'''t=int(input())
for _ in range(t):
    n=int(input())
    a=input().strip()
    tr={}
    i=0
    while a!="":
        elem=a[i]
        fi=a.find(elem)
        li=a.rfind(elem)
        if li==len(a)-1:
            li=a.find(elem,fi+1)
            a=a[li+1:]
            nb=len(a[:li+1])
        elif li!=len(a)-1:
            a=a[li+1:]
            nb=len(a[:li+1])
        elif li==-1:
            a=a[1:]

from collections import Counter
t=int(input())
           
for _ in range(t):
    n=int(input())
    a=input().split()
    ra=a[::-1]
    s=0
    i=1
    for i in range(1,len(ra)+1):
        new=ra[:i]
        tr=Counter(new)
        if all(value == 1 for value in tr.values()):
            s+=1
        else:
            break
    if s!=0:
        res=n-s
    else:
        res=n
    print(res)

'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split() 
 
    seen = set()
    unique_length = 0
    
    for i in reversed(range(n)):
        if a[i] not in seen:
            seen.add(a[i])
            unique_length += 1
        else:
            break
    print (seen)
    result=n-unique_length
    print(result)
        
    


        


    




        


    
