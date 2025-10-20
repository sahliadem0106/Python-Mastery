#soo  look may be i did something wrong with learning both lists and dicts comprehensions but its ok , let learn more about collections 
#a collection is a single "variable" used to store multiple values
#1/----- list    :  [] seperated with commas 
fruits=["apple","rfisa","coconut","louz","pineapple"]    #<====== these are elements
print(fruits)
print(fruits[2])     # we can reach each value with index , same as string   
print(fruits[0:3])    # we can choose what range of elemnts in list by 3 parametre p1:p2:p3    p1 is for the beginning and leaving it without any value means the beginning , also p2 for the ending of the list and leaving it emtoy means "to the end"  p3 is the step and leaving it empty will make it go 1 element forward ( 1 by default)
#we can iterate over a list with for
for fruit in fruits:
    print(fruit)
#also we can cheack the list length  by using len 
print(len(fruits))
#too cheack if an element is in a list we use in operator to get a booleen value 
print("zouza" in fruits)
# a list is changeable and ordered . duplicates ok
fruits[0]="zouza"   # we reassigned an existing value
print(fruits[0])   
#also we can append an element " add an element" in the end of the list
fruits.append("zabouza")
print(fruits)
#we can remove an element too
fruits.remove("louz")
print(fruits)
#insert(i, x)     → insert an element at a specific index
print("list after inserting louz again")
fruits.insert(3,"louz")
print(fruits)
# sort()     → sort the list in ascending order (in-place)
numbers=[80,20,65,43,199,20,1]
fruits.sort()        
print(fruits)
numbers.sort()
print(numbers)
fruits=["apple","rfisa","coconut","louz","pineapple"]
# reverse()        → reverse the list order (in-place)
fruits.reverse()          #reversed based on our initial order   ,,, to make it an alphabetic reverse you can simply sort and then  reverse
print(fruits)
fruits.sort()  
fruits.reverse()
print(fruits)    
# clear()    → remove all elements from the list
# index(x)         → return the index of the first occurrence of a value
print(fruits.index("coconut"))
print(fruits.count("apple"))


# ---------------- LIST METHODS SHEET ----------------

# append(x)        → add an element to the end of the list
# insert(i, x)     → insert an element at a specific index
# extend(iterable) → add multiple elements from another list/iterable
# remove(x)        → remove the first occurrence of a value
# pop(i)           → remove and return element at index (default: last)
# clear()          → remove all elements from the list
# index(x)         → return the index of the first occurrence of a value
# count(x)         → count how many times a value appears
# sort()           → sort the list in ascending order (in-place)
# sort(reverse=True) → sort the list in descending order
# reverse()        → reverse the list order (in-place)
# copy()           → return a shallow copy of the list
# len(list)        → return the number of elements in the list
# in operator      → check if an item exists in the list
# slicing [i:j]    → get a sublist from index i up to (but not including) j
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
print("###############################################")
print("###############################################")
print("###############################################")
print("SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEETS")
#a set is unordered and immutable but we can add and remove . no duplicates
cars={"BMW","AUDIE","MCLAREN","polo","volkswagen","volkswagen"}   #sets works usually with constants , also as u see even if i added another "volkswagen"  it ignored it , it still count 1 "volkswagen"
print(cars)
print(len(cars))
print("mazda" in cars)
#we can reach items by index in sets bcs they are unordered
#also we cant actually change a value in a set ,but we can add and remove a value
cars.add("mazda")    #it just adds it (remember no order)
print(cars)
cars.remove("AUDIE")
print(cars)
cars.pop()    #pop will remove what ever element is first ( it will be random)
print(cars)
cars.clear()  #to clear all the set

# ---------------- SET METHODS SHEET ----------------

# add(x)         → add an element to the set (duplicates ignored)
# remove(x)      → remove an element; raises error if not present
# discard(x)     → remove an element if present; does nothing if not
# pop()          → remove and return an arbitrary element (sets are unordered)
# clear()        → remove all elements from the set
# update(iterable) → add multiple elements from another iterable
# union(other_set) → return a new set with all elements from both sets
# intersection(other_set) → return a new set with elements common to both
# difference(other_set) → return a new set with elements in the first set but not in the second
# symmetric_difference(other_set) → return elements in either set, but not both
# issubset(other_set) → check if all elements of this set are in other_set
# issuperset(other_set) → check if this set contains all elements of other_set
# isdisjoint(other_set) → check if sets have no elements in common
# len(set)       → return the number of elements in the set
# in operator    → check if an element exists in the set
# frozenset()    → create an immutable set (cannot add/remove elements)

#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
print("###############################################")
print("###############################################")
print("###############################################")
print("                           TUUUUPLEEEEES")

#tuples are ordered and unchangeable ,duplicates ok , fast
countries=("tunisia","ksa","Qatar","palestine","bermuda","bermuda")
print(len(countries))
print("syria" in countries)
print(countries.index("tunisia"))   #tun is at 0
print(countries.count("bermuda"))  # count the duplicates of a value in the tuple
for country in countries:
    print(country)
print(countries)

# ---------------- TUPLE CHEAT SHEET ----------------

# Tuples are ordered, immutable (unchangeable), allow duplicates, and are faster than lists.

# count(x)       → return how many times a value appears in the tuple
# index(x)       → return the index of the first occurrence of a value
# len(tuple)     → return the number of elements in the tuple
# in operator    → check if an item exists in the tuple
# slicing [i:j]  → get a subtuple from index i up to (but not including) j
# concatenation (+) → combine two tuples into a new one
# repetition (*) → repeat a tuple’s elements multiple times
# tuple(iterable) → create a tuple from another iterable

# Note: tuples are immutable → no add, remove, or change operations allowed
# Elements can be of mixed data types (numbers, strings, etc.)
# Tuples can be nested (tuples inside tuples)
# Tuples can be used as dictionary keys or set elements (because they are immutable)
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
print("###############################################")
print("###############################################")
print("###############################################")
print("                            DICIIIIIICTS")
#dictionary is a collection of {key:value} pairs ordered and changeable with no duplicates in it 
capitals={
    "USA":"Washington D.C",
    "India" : "New Dalhi",
    "China" :"Beinjing",
    "Russia":"Moscow"}
print(capitals.get("USA"))    # dict.get(key)    → access value safely, returns None or default if key missing
if capitals.get("Russia"):
    print("that capital exist")
else:
    print("that capital dosen't exist")
capitals.update({"Germany":"berlin"}) 
capitals.update({"USA":"Detroit"})    # dict.update(other_dict) → update dictionary with another dict (overwrites keys) , we can inserta new  key:value pair update an existing one
print(capitals)
capitals.pop("China")    # dict.pop(key)    → remove a key:value pair
print(capitals)
capitals.popitem()   # dict.popitem()   → remove last inserted key-value pair
print(capitals)
keys = capitals.keys()
print(keys)  #  dict_keys(['USA', 'India', 'Russia'])   : It’s a dict_keys view object (iterable, behaves like a set, updates with the dict).
for key in keys:
    print(key)
values=capitals.values()
print(values)    #dict_values(['Detroit', 'New Dalhi', 'Moscow'])  : It’s a dict_values view object (iterable, behaves like a set, updates with the dict).
for value in values:
    print(value)
items=capitals.items()    #items a dic object wich resembles a 2d list of tuples
print(items)
for key,value in capitals.items():
    print(f"{key}:{value}")







# ---------------- DICTIONARY SHEET ----------------

# Dictionaries store key-value pairs (unordered, mutable, no duplicate keys).

# dict[key]        → access the value for a given key (error if key missing)
# dict.get(key)    → access value safely, returns None or default if key missing
# dict.keys()      → return all keys as a view object
# dict.values()    → return all values as a view object
# dict.items()     → return all key-value pairs as tuples
# dict.update(other_dict) → update dictionary with another dict (overwrites keys)
# dict.pop(key)    → remove and return value for a key
# dict.popitem()   → remove and return last inserted key-value pair
# dict.clear()     → remove all items from the dictionary
# dict.copy()      → return a shallow copy of the dictionary
# dict.setdefault(key, default) → return value if key exists, else insert key with default
# len(dict)        → return the number of key-value pairs
# in operator      → check if a key exists in the dictionary
# del dict[key]    → delete a key-value pair

# Note:
# - Keys must be immutable (e.g., strings, numbers, tuples)
# - Values can be any data type
# - No duplicate keys allowed (new value overwrites old one)
