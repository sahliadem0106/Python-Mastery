from collections import Counter
ch=input()
nb=Counter(ch)
c=0
for k,v in nb.items():
    if v==1:
        c+=1
if len(nb.keys())%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
