"""
A dictionary lets you get the value of a key at sonstant time
"""
#defining a dictionary
first_dict = {}
second_dict = dict()

#print(type(first_dict))
#print(type(second_dict))

fruit_basket = {
    "mango":40,
    "apples":24,
    "orange": "beautiful", 
    "pawpaw":["yellow","green"]
    }

#print(len(first_dict))
#print(len(fruit_basket))

# mangoes = fruit_basket["mango"]
# print(f"We have {mangoes} mangoes in the basket")

# apples = fruit_basket.get("berrys", 0)
# print(f"We have {apples} berry's in the basket")

# #gets all the keys
# all_fruit_keys = fruit_basket.keys()
# print(all_fruit_keys)

#add new keys and values
# fruit_basket.update({"berrys":24})
# print(fruit_basket.items())

# #remove a key and its value, while popitem() removes the last item in the dictionary
# fruit_basket.pop("berrys")
#or 
#del fruit_basket("berrys")
"""
But be careful 'del' doesn't just delete the values in a list, dict, var, etc. it also deletes thr object itself
"""

#To clear basket
# fruit_basket.clear()

# print(fruit_basket)

#To copy a dictionary
new_fruit_basket = fruit_basket #This does not copy it only references
#print(id(fruit_basket)) and print(id(new_fruit_basket)) will return the same id
#Shallow copy uses the reference of the copiee, so when the original changes, the copy also changes
#Deep Copy creates its own reference, the recursively insert copies from the object found in the original

# new_fruit_basket1 = fruit_basket.copy() #Still shallow copy
# new_fruit_basket2 = copy.deepcopy(fruit_basket) #deep copy


item_i = ["beans", "rice", "yam"]
item_j = ["stew", "egg", "vegetable"]

for index, item2 in enumerate(item_i):
    print(f"{index} and {item2}")

for i in item_i:
    for j in item_j:
        print(i, " and ", j)

for key, value in fruit_basket.items():
    print(key, " = ", value)