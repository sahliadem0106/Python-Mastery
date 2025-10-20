#for loops = execute a block of code a fixed number of times (we have bg and end ), i can iterate over a range , string , sequence , etc 
for x in range(1,11):
    print(x)
#lets do it backwards
for x in reversed(range(1,11)):
    print(x)
print("BOMBACLAAT")
#if we want to count with steps we can use 
for x in range(1,11,3):     #third parametre is the step  ( how much to skip)
    print(x)
#------------------------
creditcard="1234-56789-9012-3456"
for x in creditcard:
    print(x)             # here x will represent a caracter , one by one 
#continue and break
for x in range(1,21):
    if x==13:
        continue    #its made to skip iteration number 13
    else:
        print(x)   #process
for x in range(1,21):
    if x==13:
        break    #it will stop at 13 (will not print 13)
    else:
        print(x)   #process 
######################## WHILE
#while loops : execute some while  some condition remains true 
name=input("enter ur name bro")
while name=="":
    print("please ur name bro")
    name=input("enter ur name bro")
print(f"hello {name}")
age=int(input("eyoo bro , type ur age for me "))
while age <10:
    print("MAMAAAAAA  your son is using the laptop")
    age=int(input("again fast!"))
print(f"your age is {age} , welcome habibi")
food=input("enter a food you like (q to quit):")
while not food =="q":
    print(f"you like {food}")
    food=input("enter a food you like (q to quit):")
print("saha ou bechfee")
num=int(input("enter num between 1 and 100"))
while 1>num or num>100:
    print("again")
    num=int(input("enter num between 1 and 100"))
print(f"your num :{num}")
##nested loop
for x in range(3):
    for y in range(1,10):
        print(y ,end="")
    print()
#pyramideeeee:
rows=int(input("give me da rows"))
cols=int(input("give me da cols"))
sym=input("give me da sym")
for x in range(rows):
    for y in range(cols):
        print(sym ,end="")
    print()
def pyra(layers:int):
    for i in range(1,layers+1):
        stars='*'*(2*i-1)
        print(stars.center(2*layers-1))     #  .center(nb of spaces)
pyra(9)



