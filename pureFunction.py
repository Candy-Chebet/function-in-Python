#Pure functions affect nothing out of it.
#i.e. they do not affect the global area of the program.
# They affect variable that are only within th function itself.

#Here is an example
list = [1,2,3]  # multiple of this will not be the one printed.

def multiply_by2(list):
    new_list = []
    for item in list:
        new_list.append(item*2)
    return new_list

print (multiply_by2([10, 20, 30,])) 