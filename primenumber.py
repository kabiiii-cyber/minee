# prime /not

#taking user input
num = int(input("enter a number:"))


# checking and displaying results

if (num):
  print(num,"prime number")
else:
  print(num,"not prime number")


def is_prime(number):
  if number < 2:
      return False
  else:
      return True

  for i in range(2, int (number **0.5)+1) :
    if number % i == 0 :
      return false
    else:
      return true
  num = int(input("enter number:"))

  if is_prime(num):
    print(num,"prime number")
  else:
    print (num,"not prime number")

