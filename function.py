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

##############################

def say_hello(name, surname):
    print(f"hello, {name} {surname}")
	
say_hello("Bob", "smith")


def divide(dividend, divisor):
    if divisor != 0:
	    print(dividend / divisor)
	else:
	    print("You fool")


divide(dividend=15, divisor=0)
