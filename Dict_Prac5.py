dict = {'apple': 3, 'banana': 5, 'cherry': 2}

#pop item
item = dict.popitem()
print('Removed: ', item)
print("Updated dict: ", dict)

#values
print("Values: ")
for val in dict.values():
    print(val)