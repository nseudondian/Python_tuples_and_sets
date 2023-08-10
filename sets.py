# num_set = {2, 3, 4, 5}
# strings = {"Fred", "Jude", "Greg"}
# mixed_set = {2, 3, True, "book"}

# print(type(num_set))
# print(type(strings))
# print(type(mixed_set))

# Empty set
# empty_set = set()
# print(type(empty_set)) 

# # Empty dictionary not empty set
# empty_dict = {}
# print(type(empty_dict))





# Some set operations

# add(): it takes a single argument and adds it to the set

# num_set = { 3, 12, 4, 9, 10}

# num_set.add(20)
# num_set.add(20)

# print(num_set)











#len()- returns the number of elements in a set

# num_set = { 3, 12, 4, 9, 10}

# set_length = len(num_set)
# print(set_length)











# remove() - removes an element from a set and return no output

# num_set = { 3, 12, 4, 9, 10}

# num_set.remove(10)
# num_set.remove(3)


# print(num_set)









# clear() - empties the set out 

# num_set = { 3, 12, 4, 9, 10}
# num_set.clear()
# print(num_set)












# Intersection: returns new set with members common to left and right set. Denoted by an ampersand &


# dev = {"Java", "C", "Python", "SQL"}
# data = { "excel", "Python", "SQL", "R"}

# print(dev & data) 



# Union: returns a new set that has all members of both sets combined.
#  denoted by the Pipe character |.

# dev = {"Java", "C", "Python", "SQL"}
# data = { "excel", "Python", "SQL", "R"}



# print(dev|data)

# x = {4, 5, 6}
# y = {8, 9, 10}
# print(x|y)



# Difference: Returns a new set with values in the left side that are not in the right side. Denoted by the minus sign -.

dev = {"Java", "C", "Python", "SQL"}
data = { "excel", "Python", "SQL", "R"}

# print(dev - data)
# print(data - dev)


# x = {4, 5, 6, 10}
# y = {8, 9, 10}
# # print(x - y)
# print(y - x)

