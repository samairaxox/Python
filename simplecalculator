def addition(n1,n2):
    return n1+n2
def subtraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
all = { "+" : addition , "-" : subtraction , "*" : multiplication , "/" : division}

def calculator():
    should_accumulate = True
    x=float(input("Enter your first number:"))
    while should_accumulate:
       print("+\n-\n*\n/")
       y =input("Pick an operation")
       z = float(input("What's the next number:"))
       if y in all:
          result = all[y](x,z)
          print(f"{x}{y}{z} = {result}")
       
          choice = input(f"Type 'y' to continue with {result} and n for new calculation")
          if choice.lower() == "y":
           x = result
          else:
           should_accumulate = False
       else:
          print("Invalid operation")
          
       
calculator()
