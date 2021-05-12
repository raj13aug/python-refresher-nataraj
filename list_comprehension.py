numbers = [1,3,5]
doubled = []
#simple type
for num in numbers:
    doubled.append(num * 2)
print(doubled)

#list comprehension
doubled = [ num * 2 for num in numbers]
print(doubled)


starts_s = []
#simple method
friends = ["Shamantha", "Saurab", "Jen"]
for friend in friends:
  if friend.startswith("S"):
    starts_s.append(friend)

print(starts_s)

#list comprehension

friends = ["Sam", "Shamantha", "Sarabh"]
starts_s = [friend for friend in friends if friend.startswith("s")]
print(starts_s)
print("friend: ", id(friends), "starts_s:", id(starts_s))

#id is represent is storage location
