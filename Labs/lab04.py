#Question 2: Write a function find_word(sentence, word) that takes 'sentence' (a string) and 'word' (another string) as parameters 
# and returns the index of the first occurrence of 'word' in 'sentence'. As with the previous question, 'word' in this case can be any string, 
# it is not necessarily a standalone English word that is normally surrounded by spaces. You may assume that 'sentence' has at least one character in it, 
# and that 'word' exists in 'sentence'.
def find_word(sentance, word):
    x = sentance.find(word)
    return x

print(find_word('stubby tubby chubby gubby', 'tubby'))
print(find_word('1213141516171819', '1'))
print(find_word('XXXXY', 'Y'))
print(find_word('ABCDEFG XY', 'X'))
print(find_word('great day I lay you may have clay and play', 'you'))



#Question3: Write a function word_swapper(sentence, word) that takes 'sentence' and 'word' as parameters, replaces every 'word' in the 'sentence' with 'ABC'. 
# You may assume the string has at least one character in it.
def word_swapper(sentence, word):
    x = sentence.replace(word, 'ABC')
    return x

print(word_swapper('This is a sentence.', 'is'))
print(word_swapper('coding is cool but coding is hard!', 'cod'))
print(word_swapper('coding is cool but coding is hard!', 'co'))
print(word_swapper('ha! ha! ha! ha! hahaha!', 'haha'))
print(word_swapper('ha! ha! ha! ha! hahaha!', 'huh'))


#Question 4: Write a function replace_character(sentence) that takes a parameter 'sentence' returns a new string where all letters 's' and 'S' are replaced with '$'. 
# You may assume the string has at least one character in it.
def replace_character(sentance):
    x = sentance.replace('s', '$')
    x = x.replace('S', '$')
    return x

print(replace_character('stubby tubby chubby gubby'))
print(replace_character('1213141516171819'))
print(replace_character('I saw Sam somewhere'))
print(replace_character('abcdefghijklmnopqrstuvwxyz'))
print(replace_character('singing a song makes you feel good'))

#Question 5: Write a function top_and_tail(string) that takes a string as a parameter and returns the string with its first and last characters removed. 
# You may assume the string has at least one character in it.
def top_and_tail(string):
    return string[1:-1]

print(top_and_tail('stubby'))
print(top_and_tail('another test string'))
print(top_and_tail('X'))
print(top_and_tail('XY'))
print(top_and_tail('XYZ'))

#Question 6: Write a function half_string(string) that takes a string as a parameter and returns the first half of the string. You may assume the string has at 
# least one character in it. If the string length is odd, then you may assume it returns (𝑛−1)2 characters where n represents how many characters are in the 
# original string (e.g., string = 'hello', returns 'he').
def half_string(string):
    return string[:int(len(string)/2)]

print(half_string('stubby'))
print(half_string('spongebob'))
print(half_string('a'))
print(half_string('XY'))
print(half_string('XYZ'))

#Question 7: Write a function second_half_string(string) that takes a string as a parameter and returns the second half of the string. You may assume the string
# has at least one character in it. If the string length is odd, then you may assume it returns (𝑛+1)2 many characters (e.g., string = 'hello', returns 'llo') 
# where n represents the number of characters in the original string.
def second_half_string(string):
    return string[int(len(string)/2):]

print(second_half_string('stubby'))
print(second_half_string('spongebob'))
print(second_half_string('a'))
print(second_half_string('XY'))
print(second_half_string('XYZ'))


#Question 8: Write a function first_nth_string(string, n) that takes a string string and an integer n as parameters and returns the sliced string of the first n characters. 
# You may assume that string contains at least n + 1 characters.
def first_nth_string(string, n):
    return string[:n]

item = first_nth_string("this is some string", 4)
print(item)
item = first_nth_string("this is some string", 7)
print(item)
item = first_nth_string("this is some string", 0)
print(item)
item = first_nth_string("this is some string", 19)
print(item)

#Question 9: Write a function full_name(first_name, last_name) that takes a person's first name and last name as parameters and returns their full name made up of 
# the first name, a space character and their last name all concatenated together.
def full_name(first_name, last_name):
    return first_name + " " + last_name 
name = full_name('Alex', 'Ng')
print(name)
print(full_name('Malcolm', 'X'))
print(full_name('Wanda', 'Fish'))
print(full_name('alex',''))
print(full_name('', 'bozo'))


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



#Question 11: Write a function sorted_items(data) that takes data as a parameter and returns a sorted list.
def sorted_items(data):
    return sorted(data)
count = sorted_items([1, 2, 3, 4, 5])
print(count)
count = sorted_items([1, 2, 1, 2, 1, 2])
print(count)
count = sorted_items(['a', 'b', 'c', 'a', 'a', 'a'])
print(count)
count = sorted_items([9, 7, 5, 3, 1])
print(count)



#Question 12: Write a function third(data) that takes a list argument and returns the third element of that list. You may assume that the parameter data contains at least three elements.
def third(data):
    return data[2]
#Test Cases
item = third([10, 20, 30, 40, 50])
print(item) #answer is 20

item = third(['cat', 'dog', 'cow', 'chicken', 'crow'])
print(item) #answer is 'cow'

#Question 13: Write a function insert_item_end(data, item) that takes a list data , and item  as a parameter and returns a new list that contains item at the end of the data using the insert method (i.e. you cannot use append). 

def insert_item_end(data, item):
    data.insert(len(data), item)
    return data

#Test cases
count = insert_item_end([1, 2, 3, 4, 5, 6], 1)
print(count)
count = insert_item_end([1, 2, 1, 2, 1, 2], 2)
print(count)
count = insert_item_end(['a', 'b', 'c', 'a', 'a', 'a'], 'a')
print(count)
count = insert_item_end(['a', 'b', 'c', 'a', 'a', 'a'], 'c')
print(count)


#Question 14: Write a function append_list_new(data1, data2) that takes two lists data1 and data2 as a parameter and returns a new list that appends them both in the order of  data1 and then data2 .  Make sure that your new list is not referencing the old lists' items.

def append_list_new(data1, data2):
    a = data1.extend(data2)
    print(a)
count = append_list_new([1, 2, 3,7, 4, 5], [1])
print(count)



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
	
#Test Cases
item = nth_element([10, 20, 30], 0)
print(item)
item = nth_element(['bob', 'carol', 'ted', 'alice'], 3)
print(item)
last_item = remove(["a", "list", "of", "words"])
print(last_item)
last_item = remove(["kill", "bill"])
print(last_item)


#Question 19: Write a function duplicate_last(data) that takes a list as a parameter and returns a new list containing all the elements of the parameter data but with the last item appearing twice. Your function should not modify the list it is given. 

def duplicate_last(data):
    return data[:] + [data[-1]]

#TestCases
item = duplicate_last([1,2,3])
print(item)
item = duplicate_last(['hi'])
print(item)
item = duplicate_last([10])
print(item)
item = duplicate_last(['a','b','c'])
print(item)

#Question 20: Write a function cubed_tuple(number) that takes a number argument and returns a tuple consisting of the number with the number cubed. See below for examples.
def cubed_tuple(number):
    return (number, number*number*number)

#Test Cases
print(cubed_tuple(1))
print(cubed_tuple(3))
print(cubed_tuple(0))

#Question 21: Write a function list_swap(lst) that takes a list lst as a parameter and swaps pairs of consecutive values in the list i.e. index 0 and 1, 2 and 3, 4 and 5 and so on. If there are odd number of elements in the list, the last element remains the same. For instance, list_swap([1,2,3,4,5]) returns [2,1,4,3,5]
def list_swap(lst):
    for index in range(len(list)):
        thub 



#Question 22: Write a function num_words(string) that takes a string argument and returns a count of the number of words in the string, 
# where a word is defined as a maximal-length sequence of characters other than "white space" characters.
def num_words(string):
    x=string.split()
    return len(x)

#test cases
word_count = num_words("Welcome to lists!")
print(word_count)	
word_count = num_words("thi01234&*9 &^%x 1")
print(word_count)
word_count = num_words("20")
print(word_count)
word_count = num_words("hah!")
print(word_count)


#Question 23: Write a function list_sorting(lst1,lst2) which takes two lists: lst1 and lst2. Lst1 and lst2 are to contain the names of the employees 
# and their ages respectively. Your function needs to return copies of these lists such that they are both sorted in order of age (descending order) 
# (ie the names of employees in the lst1 are also required to be ordered according to their ages in lst2). If two or more employees have the same age 
# then these employees need to be ordered by their names also (this time in ascending order: A-Z).

def 