import random
names=["Mariya","Gendalf","Batman"]
profs=["programmer","wizard","superhero"]
#lets combine them into a dict
dict={}
#option 1: zip function
for (key,value) in zip(names,profs):
    dict[key]=value    #we will pair both lists together and as a result , stores each of the names as a key and each of the profs as a value 
print(dict)
#or  we can use range(n)   , we will iterate over the total length  of the list using range  BUT actually  we are not iterating over the list items , we are pairing items with the same index or order
for x in range(3):
    dict[names[x]]=profs[x]
print(dict)
#dict comprehension with zip
dict1={key:value for (key,value)in zip(names,profs)}    #we will put the formulaire
print(dict1)
#dict comprehension with for range
dict2={names[i]:profs[i] for i in range(len(names))}
#------------------------------
my_dict={
    "spider":"photographer",
    "Bat":"philanthropist",
    "wonder wo":"nurse"
}
my_dict={(key+"man" if key!="spider" else "Superman"):(val if val!="photographer"  else "journalist") for (key,val) in my_dict.items()}    #here we are saying that add man if its different to spider | else key will have value like instead of kay+man it became a string
print(my_dict)
#if we want to add condition we simply put them in ()
#------------------------EX2 : DNA  dictionary of lists --------------------------
bases=["A","T","C","G"]
strand1=random.choices(bases,k=10)   #k is length
print(strand1)
def sync(val:int):
    if val=="T":
        return "A"
    elif val=="C":
        return "G"
    elif val=="G":
        return "C"
    else:
        return "T"
dna={key:[val,sync(val)] for (key,val) in enumerate(strand1)}        #[val,sync(val)] this is a list so we jsut made a dictionary of lists
print(dna)   #enumerate will track the items them selfs and unpack them into val , also it will track the order in the list givin by key
#-----------------------------EX3: lists of dictionary go dictCOMPREHENSION2.py  ------------------------
