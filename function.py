def hello():
  print("Hello")

hello()


print("Welcome to the age in second program")

def user_age_in_seconds():
  user_age = int(input("Enter your age: "))
  age_seconds = user_age * 365 * 24 * 60 * 60
  print(f"your age in seconds is {age_seconds}")

user_age_in_seconds()

print("Goodbye")
