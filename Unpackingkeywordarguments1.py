def named(**kwargs):
    print(kwargs)
	
	
name(name="Bob", age=25)

######################################33

def named(**kwargs):
    print(kwargs)
	
details = {"name": "Bob", "age": 25}
named(**details)

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def named(**kwargs):
  print(kwargs)
	
def print_nicely(**kwargs):
  named(**kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")
		
print_nicely(name="Bob", age=25)

################################

# note: **kwargs is the named arguments into kwargs.
# notes: all the positional arguments into args

def both(*args, **kwargs):
    print(args)
	print(kwargs)
	
both(1,2,3, name="Bob", age=25)
