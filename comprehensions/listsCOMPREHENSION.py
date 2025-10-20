# list comprehension = a concise way to create lists in python ,they are compact and easier to read than traditional loops 
#[expression for value in iterable if condition]                    <-------------------------------|
doubles = []                                                                                  #     |
for x in range(1,11):                                                                    #          |
    doubles.append(x*2)    #append add item to the list                              #              |
print(doubles)                                                                      #               |
#we can use list comprehension to make this code more compact and easier to read                    |
boubles=[x * 2 for x in range(1,20)]     #for every value in our iterable which is range here       |
print(boubles)                                                                     #                |
##                                                       ------------------------------------------>|
#for every x in this range do x*2
#expression have included append 
triples=[y*3 for y in range(1,10)]
print(triples)
squares=[z+10 for z in range(1,11)]
print(squares)
####lets work with strings
fruits = ["apple", "orange","banana","coconut"]
print(fruits)
fruit_chars=[fruit[0] for fruit in fruits]
print(fruit_chars)
##list of numbers
numbers=[0,1,-2,3,-4,5,-6,8,-7]
pos_num=[num for num in numbers if num >=0]
neg_num=[num for num in numbers if num <0]
even_number=[num for num in numbers if num%2==0]
odd_number=[num for num in numbers if num%2!=0]
converted=[abs(num) for num in numbers]
print(pos_num)
print(neg_num)
print(even_number)
print(odd_number)
print(converted)
##anothere EXE
grades = [85,42,79,90,56,61,30]
passing_gr =[grade for grade in grades if grade >=60]
print(passing_gr)