#This is a list ordered and changeable
list=["ranjith","kumar","roy"] #list
print(list)
list.append("karthi") #add at the end
print(list)
list[0]="hello" #remove ranjith by using index to overwrite
print(list)

print(list[1]) #To view index 1"kumar"

#By using loops
for y in list:
    print(list)

    #using condition to chcek true or false
    if "kumar" in list:
        print("result")
        break #break the statment
        print("hello")
print(len(list)) #to check the size of the elements

list.insert(1,"roy")
print(list)    #insert the specified name with the help of index

list.pop() #to remove the last name using pop
print(list)

del list[1]
print(list)   #to delete the specified using index

#tuples

tuples=("ranjith","kumar","roy","karthi")   #unordered and unchangeable
print(tuples)
#tuples.append("ranjith1")
print(tuples)   #error becoz it cant be add and  change

#set

thisset = {"apple", "banana", "cherry"}
print(thisset)   #Once a set is created, you cannot change its items, but you can add new items.



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)   #to remove or using discard




#Dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x = thisdict["model"] #You can access the items of a dictionary by referring to its key name

