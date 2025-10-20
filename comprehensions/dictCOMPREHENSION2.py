import string
import random
#-----------------------------EX3: lists of dictionary ------------------------
keys=["id","username","password"]
users=["mariyasha888","knotbot","batman","iyed"]
data=[{key:(i if key=="id" else users[i] if key=="username" else "".join(random.choices(string.printable,k=10))) for key in keys } for i in range(len(users))]    # random.choices  → returns a list of random elements chosen from a sequence and the sequence here is string.printable   and "".join() combines elemnts of a list in one string   
print(data) 