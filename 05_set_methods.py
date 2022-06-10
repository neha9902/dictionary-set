b = set()
print(type(b))
b.add(6);
b.add(7)
print(b)

# b.add([5,8,9])  List can not be added as we change it
# print(b)

b.add((4,7,8))   # tuple can be added as it's content can not get changed
print(b)

# b.add({9:0})   dictionary  also can not be added

print(len(b))
b.remove(6)
print(b)