# 4operators
#1numbers
#operators
#2number
#else wrong operator



def add(x,y):
  return x+y

def subtract(x,y):
  return x-y

def divide(x,y):
  return x/y

def multiply(x,y):
  return x*y

# man program
print("select operator")
print(" 1 add")
print("2 subtract")
print("3 multiply")
print("4 divide")


# input from user
choice = input("chose(1/12/3/4): ")

if choice in (1,2,3,4):
  num1 =float
