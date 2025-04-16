#Create a dictionary
dict = {'name': 'Alice', 'Age': 30, 'city': 'Paris'}

#use the get method
print("Name: ", dict.get('name', 'Not Found'))
print("Name: ", dict.get('Age', 'Not Found'))

#Clear the dict
dict.clear()
print("Dictionary after clear():", dict)
