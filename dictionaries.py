friends = [
{"name": "nataraj", "age": 25},
{"name": "vino", "age": 2},
{"name": "mano", "age": 5},
]

print(friends[0]["name"])


student_data = {"Ram": 50, "vino": 98, "shamantha": 89}

for student in student_data:
  print(student, ": ", student_data[student])
  print(f"{student} : {student_data[student]}")


#items() --> studendance.items() give you two values for each student that you can get as two separate variables here in python.

student_data = {"Ram": 50, "vino": 98, "shamantha": 89}

for key,value in student_data.items():
  print(f"items value : {key}:{value}")

#for loop using dict
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

if "Bob" in student_attendance:
  print(f"Bob: {student_attendance['Bob']}")
else:
  print("Bob is not a student in this class")

#Average of value:

average_value = student_attendance.values()
total = sum(average_value) / len(average_value)
print(total)
