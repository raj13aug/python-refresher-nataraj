users = [
    (0, "Bob", "password"),
	  (1, "Rolf", "bob123"),
	  (2, "Jose", "long4assword"),
	  (3, "username", "1234"),
]
print(users[0])
username_mapping = {user[0]: user for user in users}
print(username_mapping)


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
  print("Your details are correct!")
else:
  print("your details are incorrect")
