mylist = ["Apple","Banana","Mango","cherry", "orange", "kiwi", "melon", "mango"]
mylist1 = [1,2,3,4,5,6,7,8,9,10]
print(mylist)
print(mylist[1]) # index
print(len(mylist)) # length of list
print(type(mylist)) # type of mylist 
print(type(mylist1)) # type of mylist1 
print(mylist[-1]) # negitiv index
print(mylist[2:5]) # print a 2 to 5 index to print a values
print(mylist + mylist1) # concet 2 list
print(mylist1 * 4) # 3 time repit

if "Apple" in mylist: # if condition
    print("yes")

mylist[3] = "Apple" # chang a values of 3td index
print(mylist)

mylist.append("Jamu") # add to a last of value 
print(mylist) 

mylist.insert(2,"pinopal") # 2 index to a insert 
print(mylist) 

mylist.remove("Apple") # remove to a values
print(mylist)

mylist.pop() 
print(mylist)

del mylist[0] # delet to a indexing to 0  
print(mylist)

mylist.clear() # all of to a clear / delet
print(mylist) 





