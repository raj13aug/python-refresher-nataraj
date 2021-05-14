#destructring values
t = 5, 11
x,y = t
print(x,y)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("harry", 32, "Lecturer")]

for name, age, profession in people:
print(f{"Name": {name}, Age:{age}, profession: {profession}})



#underscore on its own is so bad a variable name, that nobody would wanna use it which python community has decided.

person = ("Bob", 42, "Mechanic")

name, _, profession = person

print(name, profession)

head, *tail = [1,2,3,4,5] # first value in here will become the head and then this syntax here will collect the other values.


print(head)
print(tail)
