#sort : Sorts the list
#type : Print the type of datatype
#append: Add element at the end 
#extend: Adds multiple elements in the list 
#index: which searches for a given element from the start of the list and returns the lowest index where the element appears. 
#max: Returns maximum element in the list 
#min: Returns minumum element in the list 
#len: Returns the length of the list 
#clear:  Removes all element from the list 
#Insert: insert(index,element) elem is inserted to the list at the ith index. All the elements after elem are shifted to the right.
#count: method returns the number of elements with the specified value.
#pop(index[optional]): removes elements from the list,if the element doesnt exist it throws error  
#remove: Removes element from the list, if the element doesnt exist it throws error 
#reverse: Reverses a list 
#len: returns length of the list


list=[40,20,10,90]

print(list)
list.sort()
print(list)
print(type(list))

print(list)
list.extend([2,3,4])
print(list)
print(list.index(20))
print(max(list))
print(min(list))
list.clear()
print(list)
list.insert(0,10)
list.append(20)
list.append(30)
list.append(40)

print(list)
print(list.count(10))
list.pop(0)
print(list)
list.remove(30)
print(list)
list.reverse()
print(list)
list_2=list.copy()
print(list_2)

