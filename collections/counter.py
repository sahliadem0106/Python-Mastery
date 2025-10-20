#1/ lets create a counter
import collections
from collections import Counter
#using a list :
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_counter = Counter(fruits)
print(fruit_counter) #fruit_counter is a Counter object that shows each fruit and how many times it appears. The output looks like a dictionary with key:existing_times pair , but it’s a Counter object with extra functionality.
#using a string :
text = "hello"
text_counter = Counter(text)
print(text_counter)
# a dictionary (manually specified counts) :
manual_counter=Counter(apple=5,banana=9,orange=2)
print(manual_counter)
#an empty one
empty_counter = Counter()
print(empty_counter)
#---------------------------------------
#---------------------------------------
print("#############################################")
print("#############accessing counts################")
print("#############################################")
#after are creating counters to use the values in result , so lets access the counts
#we can access the count of any item using dictionary-like syntax. If an item doesn’t exist in the Counter, it returns 0
print(fruit_counter["apple"]) 
print(fruit_counter["mango"])
#---------------------------------------
#---------------------------------------
print("###############################################")
print("#############updating a counter################")
print("###############################################")
#we can update a Counter with new data using the update() method, which adds counts from another iterable or Counter.
more_fruits = ["apple", "mango", "banana"]
fruit_counter.update(more_fruits)           #counter1.update("counter2")   its like adding elements , so when it counts again it gives another result
print(fruit_counter)
#"apple" and "banana" counts increased, and "mango" was added with a count of 1
#---------------------------------------
#---------------------------------------
print("##########################################################")
print("############# Common methods & Operations ################")
print("##########################################################")
print("most_common(n) : ")
#most_common(n): Returns the n most common items and their counts as a list of tuples. If n is omitted, it returns all items sorted by count (highest to lowest).
print(fruit_counter.most_common(3))
#elements(): Returns an iterator over the elements, repeating each one according to its count and the result will be putted in a list   its sorted (highest to lowest).
print(list(fruit_counter.elements()))
#add counters
Counter1= Counter(apple=3,bananza=2)
Counter2=Counter(apple=1,bananza=1,orangina=1)
print(Counter1+Counter2)
#"orangina" was added with a count of 1
#substract counter
print("case 1 of subtracting")
print(Counter2-Counter1)   
#in this case we subtracted counter 1 from counter 2 1-3=-2,1-2=-1,1-0=1 in this case it only showed the items and its counts with >=0 counts "orangina"
print("case 2 of subtracting")
print(Counter1-Counter2) 
#in this case we subtracted counter 2 from counter 1      3-1=2,2-1=1,orangina didnt exist in counter one so there is no subtracting for it
#---------------------------------------
print("#########################################################################")
print("############# subtacting and maintaining negative values ################")
print("#########################################################################")
#A Counter can store negative or zero counts, which is useful in scenarios like tracking differences or deficits.we use counter1.subtract(counter2)  instead if "-"
counter3=Counter(apple=3, banana=2)
counter3.subtract(apple=5,banana=2)
print(counter3)
#---------------------------------------
print("###################################################")
print("############# Clearing & resetting ################")
print("###################################################")
fruit_counter.clear()
print(fruit_counter)
#Counter is simple, efficient, flexible, and readable, it avoids manual loops, runs fast, works with any hashable items, supports advanced operations, and makes code cleaner.
# Counter - Real-World Use Cases:
# - Text analysis: word/char frequencies in text
# - Data processing: tally votes, surveys, inventory
# - Algorithms: frequency analysis, duplicates, most common elements
# - Difference tracking: compare datasets (sold vs. returned)

# Things to Keep in Mind:
# - Keys must be hashable (str, int, tuple) → lists/dicts not allowed
# - Memory: large unique datasets = higher memory usage
# - Order: preserves insertion order (Python 3.7+)
