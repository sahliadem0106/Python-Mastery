# defaultoooo dictoooo timooooooo
# Think of a regular dictionary: If you try to access a key that doesn't exist, it raises a KeyError. With defaultdict, instead of an error, it creates a default value for that key on the fly.

print("##########################################################")
print("#############  creating a deafault dict   ################")
print("##########################################################")

# first we import from collections
from collections import defaultdict

# default to empty list 
group_dict = defaultdict(list)      # <=== value is a list

# default to 0 (using int)
count_dict = defaultdict(int)     

# default empty set (using set)
set_dict = defaultdict(set)

# or also we can make a custom default (using a lambda function)
custom_dict = defaultdict(lambda: "default value")

print("##########################################################")
print("############# accessing and adding value  ################")
print("##########################################################")

# if we used a simple dict and tried to print an unknown key it will raise keyerror here,
# to add to a defaultdict we use dd["keyname"].append(value)

# Now lets add to the group_dict 
group_dict["fruits"].append("apple")
group_dict["fruits"].append("banana")
group_dict["veggies"].append("carrot")

print(group_dict)

#####################################

count_dict["apple"] += 1  # no error it starts at 0 and becomes 1    it creates it
count_dict["apple"] += 1  # Now 2
count_dict["banana"] += 1  # Starts at 0, becomes 1


print("##########################################################")
print("############# Common  Operations #########################")
print("##########################################################")

# it supports all regular dict methods like keys(), values(), items(), get(), pop(), etc.

# Get keys, values like a dict
print(list(count_dict.keys()))   # .keys to get keys names
print(list(count_dict.values()))   # .values()  to get value that is paired to each key 
print(list(count_dict.items()))    # items :key value pair in tuple format

########

# we can handle missing keys with .get(), returning 0 (or another default) without adding the key if it doesn't exist
print(count_dict.get("coconut", 0))   # the output is 0 and no key value pair is added  MIAWNOTE :  it just give you the value
print("mango" in count_dict)      # it will return False

# to add a key we can make a direct access [] it creates missing keys with default value
print(count_dict['grape'])      # creates grape with value 0  and print 0
count_dict["orange"] = 3       # creates orange with value 3
print(count_dict["orange"])    #print value 3     cant do this   print(count_dict['grape']=n 
print(list(count_dict.keys()))      # grape and orange are now added
print(list(count_dict.items())) 

print("setdefault() method:")
count_dict.setdefault('kiwi', 5)                      # Sets 'kiwi' to 5
print("Kiwi after setdefault:", count_dict['kiwi'])
count_dict.setdefault('apple', 10)                    # Won't change existing 'apple'
print("Apple after setdefault:", count_dict['apple']) # Still 3
print() 

# update() - Add multiple items
print("update() method:")
count_dict.update({'pear': 2, 'mango': 4})
count_dict.update([('cherry', 1)])                    # Can also use list of tuples
print("After update:", dict(count_dict))
print()

print("pop method")
# pop() - Remove and return value
grape_count = count_dict.pop('grape')                #MIAWNOTE1 : it removes the key and returns its value if the key is missing it adds the key with a default value removes it and return default (0)
print("Popped grape count:", grape_count)
print("Keys after pop:", list(count_dict.keys()))

# pop() with default value 
missing_count = count_dict.pop('watermelon', 0)       # Returns 0, no error
print("Popped watermelon (missing):", missing_count)   #MIAWNOTE1 : it removes the key and returns its value if the key is missing returns provided default (0), no factory call, no dict change
print()

# popitem() - Remove and return arbitrary key-value pair
key, value = count_dict.popitem()                     # Removes last inserted item
print(f"Popped item: {key} = {value}")
print("After popitem:", dict(count_dict))
print()

# del statement - Remove specific key
del count_dict['kiwi']
print("After del kiwi:", dict(count_dict))
print()

# clear() - Remove all items
temp_dict = defaultdict(int, {'a': 1, 'b': 2})
print("Before clear:", dict(temp_dict))
temp_dict.clear()
print("After clear:", dict(temp_dict))

print("##########################################################")
print("############# nested defaultdict #########################")
print("##########################################################")

# Dict of dicts, inner defaults to int (0)
nested_dict = defaultdict(lambda: defaultdict(int))

nested_dict["group1"]["item1"] += 1  # Creates inner dict automatically
print(nested_dict)
# Output: defaultdict(<function <lambda> at ...>, {'group1': defaultdict(<class 'int'>, {'item1': 1})})
##########MIAWNOTE1########
# Use .pop(key) when you want the defaultdict to handle missing keys with its factory 
# and ensure removal, even if it means briefly adding a key.

# Use .pop(key, default) when you need a clean, no-side-effect operation for missing keys, 
# prioritizing control and avoiding dictionary changes.
