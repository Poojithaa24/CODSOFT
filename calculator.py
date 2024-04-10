print("--------CALCULATOR--------")
ch  = 0
while ch != 7:
  print("\n-------------------------------------------")
  print("\n----Main Menu----")
  print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Square\n6.Exponent\n7.Exit")
  ch = int(input("Choose the option (1/2/3/4/5/6/7) : "))
  print()
  match ch:
    case 1:
      num1 = int(input("Enter first number : "))
      num2 = int(input("Enter second number : "))
      print(num1+num2)
    case 2:
      num1 = int(input("Enter first number : "))
      num2 = int(input("Enter second number : "))
      print(num1-num2)
    case 3:
      num1 = int(input("Enter first number : "))
      num2 = int(input("Enter second number : "))
      print(num1*num2)
    case 4:
      num1 = int(input("Enter first number : "))
      num2 = int(input("Enter second number : "))
      print(num1/num2)
    case 5:
      num1 = int(input("Enter a number : "))
      print(num1**2)
    case 6:
      num1 = int(input("Enter a number : "))
      x = int(input("Enter the power : "))
      print(num1**x)
    case 7:
      print("----Exiting---")
    case '_':
      print("Enter a valid option!!")






