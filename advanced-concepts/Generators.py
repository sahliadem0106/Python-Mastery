#i know noth about these but i will master them and understand them inshallah
#def square_numbers(nums):
    #result=[]
    #for i in nums:
        #result.append(i*i)
    #return result
#my_nums=square_numbers([1,2,3,4,5])
#print(my_nums)
# its working and everything is alright , now how can we change it to be a generator
#1/ no result variable
#2/ no return statement
#3/ replace result.append() with yield
def square_numbers(nums):
    for i in nums:
        yield(i*i)
    
my_nums=square_numbers([1,2,3,4,5])
print(my_nums)
# its showing this : <generator object square_numbers at 0x00000262515AF920>  instead of our [1,4,9,16,25]
# generators dont hold the entire result in memory , it yield one result at a time , it waiting to ask for the next result which is the first variable 
print (next(my_nums))
#we passed through the 1 to 5 list and we started looping through the list , first value "1" we yielded the 1*1  then we printed it 
#print (next(my_nums))
#print (next(my_nums))
#print (next(my_nums))
#print (next(my_nums))
#it will show StopIteration when its out of range
for num in my_nums:
    print (num)
#also if we want to make a generator object we can do it by comprehension method with just replacing the []  with () think of it like its a tuple comrehension but it will make a generator object 
#and if we want to show the genrator object in one time we just convert it to a list 
#   print (list(my_nums)) put it first for it to work , the generator will be exhausted
#   ----------------PERFORMENCE---------------------
#lets say millions of items to loop through , then having that many items in memory will be noticable  

import tracemalloc
import random
import time

# Start tracing
tracemalloc.start()

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

# Get memory usage
current, peak = tracemalloc.get_traced_memory()
print('Memory (Before): {:.2f}Mb'.format(current / 1024 / 1024))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id': i, 'name': random.choice(names), 'major': random.choice(majors)}
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {'id': i, 'name': random.choice(names), 'major': random.choice(majors)}
        yield person

#t1 = time.time()
#people = people_list(1000000)       #Memory (Before): 0.00Mb  #####Memory (After): 214.05Mb   ##Took 1.97 Seconds
#t2 = time.time()

t1 = time.time()
people = people_generator(1000000)        # memory is the same bcs the generator has not actually do anything yet its not holding the 1m value in memory ,its waiting to loop through them or grap the next one 
t2 = time.time()

current, peak = tracemalloc.get_traced_memory()
print('Memory (After): {:.2f}Mb'.format(current / 1024 / 1024))
print('Took {:.2f} Seconds'.format(t2-t1)) 
"""
==================================
ai tips and summary : 
1. WHAT IS A GENERATOR?
   - A lazy iterator that yields values one-by-one using 'yield'.
   - Created by: def functions with 'yield' OR generator expressions: (expr for var in iterable).
   - Example: def count(n): for i in range(n): yield i  # Yields 0,1,2,...,n-1 on demand.

2. KEY DIFFERENCES FROM LISTS:
   | Aspect          | List (e.g., [1]*1000000)          | Generator (e.g., (i for i in range(1000000))) |
   |-----------------|-----------------------------------|----------------------------------------------|
   | Memory          | Full allocation upfront (~N * item_size) | ~Constant (one item at a time)              |
   | Creation Time   | O(N) - builds everything         | O(1) - just an object                       |
   | Consumption     | Instant access (indexable)       | Must iterate (for/next); single-pass only    |
   | Use Case        | Random access, multiple passes   | Streaming large/infinite data               |
   | Exhaustion      | Reusable forever                 | Done after one iteration (becomes empty)    |

3. PROS:
   - Memory: Handles huge datasets (e.g., 1B rows) without OOM errors.
   - Lazy: Compute only what's needed (e.g., break early).
   - Efficient: Pipelining (chain with map/filter without full lists).
   - Infinite: yield forever (e.g., random numbers).

4. CONS:
   - Not indexable: No gen[5] - use next(gen) or loop.
   - Single-use: Can't rewind; recreate if needed.
   - Debugging: Harder to inspect (values not stored).

5. BASIC USAGE EXAMPLES:
   # Simple Generator Function
   def squares(n):
       for i in range(n):
           yield i ** 2
   
   gen = squares(5)  # Returns <generator object>
   print(next(gen))  # 0
   print(list(gen))  # [1, 4, 9, 16]  # Consumes rest
   
   # Generator Expression (Compact)
   evens = (x for x in range(10) if x % 2 == 0)
   for e in evens: print(e)  # 0 2 4 6 8 (lazy!)
   
   # Chaining (Memory-Efficient)
   data = (random.randint(1,10) for _ in range(1000000))
   filtered = (x for x in data if x > 5)  # No full list created
   total = sum(filtered)  # Only computes needed
   
   # Force to List (Loses Benefits)
   full_list = list(people_generator(1000000))  # Now uses full memory!

6. TIPS:
   - Check if generator: isinstance(gen, types.GeneratorType)
   - Send values: Use 'yield from' or .send() for advanced (coroutines).
   - Infinite: def forever(): while True: yield random.random()
   - Your Code Insight: people = people_generator(1000000)  # Just an object, 0MB!
                                    # for p in people: ...  # Now generates one-by-one.
"""