dict = {'cat': 'meow', 'dog': 'bark', 'cow': 'moo'}

#using keys
print("Keys:", list(dict.keys()))

#using pop
sound = dict.pop('dog', 'not found')
print("Popped value:", sound)
print("After pop:", dict)