








#Question 10: Write a function count_item(data, item) that takes a list data  and item as a parameter and returns an integer value that item appears in data .
def count_item(data, item):
    count = 0
    for i in range(len(data)):
        if data[i] == item:
            count = count + 1
    return count

#Test Cases	
count = count_item([1, 2, 1, 2, 1, 2], 2)
print(count) #Answer is 1
count = count_item([1, 2, 1, 2, 1, 2], 2)
print(count) #Answer is 3
count = count_item(['a', 'b', 'c', 'a', 'a', 'a'], 'a')
print(count) #Answer is 4

#Question 12: Write a function third(data) that takes a list argument and returns the third element of that list. You may assume that the parameter data contains at least three elements.
def third(data):
    return data[2]
#Test Cases
item = third([10, 20, 30, 40, 50])
print(item) #answer is 20

item = third(['cat', 'dog', 'cow', 'chicken', 'crow'])
print(item) #answer is 'cow'


#Question 14 Write a function append_list_new(data1, data2) that takes two lists data1 and data2 as a parameter and returns a new list that appends them both in the order of  data1 and then data2 .  Make sure that your new list is not referencing the old lists' items.
def append_list_new(data1, data2):
    












#Question 15: Write a function append_lists(data1, data2) that takes two lists data1, and data2  as parameters and returns a new list that contains them both in the order of data1, and then data2. Here, you cannot use extend.
def append_lists(data1, data2):
    return data1 + data2
    
#Test Cases
count = append_lists([1, 2, 3, 4, 5], [1])
print(count)
count = append_lists([1, 2, 1, 2, 1, 2], [2])
print(count)
count = append_lists(['a', 'b', 'c', 'a', 'a', 'a'], ['a'])
print(count)
count = append_lists(['a', 'b', 'c', 'a', 'a', 'a'], ['c'])
print(count)

#Question 16: Write a function furthest(data) that takes a list data as a parameter and returns the last element of the list. You may assume the list has at least one element.
def furthest(data):
    return data[-1]
#Test Cases 
last_item = furthest([10, 20, 40])
print(last_item)
last_item = furthest([1])
print(last_item)
last_item = furthest(["a", "list", "of", "words"])
print(last_item)
last_item = furthest(["fred"])
print(last_item)


#Question 17: Write a function remove(data) that takes a list data as a parameter and returns the list with the second (i.e. index 1)  element removed from the list. You may assume the list has at least 2 element.
def remove(data):
    return data[:1] + data[2:]

#Test Cases 
last_item = remove([10, 20, 40, 80])
print(last_item) 
	
last_item = remove([1, 2])
print(last_item)

last_item = remove(["kill", "bill"])
print(last_item)
	
last_item = remove(["a", "list", "of", "words"])
print(last_item)


#Question 18: Write a function nth_element(data, n) that takes a list data and an integer n as parameters and returns the nth element of the list of data, assuming the first element has an index of 0. You may assume that data contains at least n + 1 elements.

def nth_element(data,n):
    return data[n]


#Question 19: Write a function duplicate_last(data) that takes a list as a parameter and returns a new list containing all the elements of the parameter data but with the last item appearing twice. Your function should not modify the list it is given. 


