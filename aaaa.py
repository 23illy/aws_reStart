# Lists
myFruitList = ["apel", "pisang", "ceri", 1, 2, 3, 4.0, 4.1, 4.2, [10, 11, 12]]
print(myFruitList)
print(type(myFruitList))
print(myFruitList[2])
print(myFruitList[1:7])

myFruitList.append("semangka")
print(myFruitList)

myFruitList[3] = "salak"
print(myFruitList)

# Tuples
myTuple = ("apel", "nanas", "ceri", 10, 12, 14)
print(myTuple)
print(type(myTuple))

# Dictionary
myDictionary = {"Aqua": "apel", "Saanvi": "Pisang", "Paulo": "Nanas"}
print(myDictionary)
print(type(myDictionary))

# Accessing dictionary values using keys
print(myDictionary["Aqua"])   
print(myDictionary["Saanvi"]) 
print(myDictionary["Paulo"])  

# Trying to access a value that doesn't correspond to any key will result in a KeyError
# Uncommenting the following line will result in a KeyError
# print(myDictionary["apel"])
