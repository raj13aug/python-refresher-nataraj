#The return statement it returns and exists the function.

def add(x, y):
  return x + y
  print(x + y) # It won't print value because of return statement is exists.
	
	
result = add(5,8)
print(result)


def divide(dividend, divisor):
  if divisor != 0:
    return dividend / divisor
  else:
    return "You fool"

result = divide(15,3)
print(result)
