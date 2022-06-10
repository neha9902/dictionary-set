myDict = {
    "a" : "Apple is a fruit",
    "b" : "Ball",
    "c" : "cat",
    "marks" : [1,5,9,0],
    "anotherdict" : {"tommy":"player"},
    1 : 78
}
# print(myDict.keys())
# print(type(myDict.keys()))
# print(type(myDict))
# print(list(myDict.keys()))
# print(myDict.values())
# print(myDict.items())

# print(myDict)
# updateDict = {
#     "anu":"friend",
#     "ram":"friend"
# }
# myDict.update(updateDict)
# print(myDict)

print(myDict.get("a"))
print(myDict["a"])

print(myDict.get("a1"))  # does not throw error
#print(myDict["a1"])       # throw an error as a2 is not present in myDict
