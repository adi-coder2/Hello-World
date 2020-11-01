def calc():
  a = float(input("Enter first number:"))
  b = float(input("Enter second number:"))
  
  
  print("Select operation to be carried:")
  print("1.+ (Addition)")
  print("2. - (Substraction")
  print("3. * (Multiplication)")
  print("4. / (Division)")

  op = int(input("Your Option:"))

  if op == 1:
	  print(a + b)
  elif op == 2:
	  print(a - b)	
  elif op == 3:
	  print(a * b)	
  elif op == 4:
	  print(a / b)
  else:
	  print("Oops Invalid operation, please select from the options (1,2,3,4)")
	  
calc()

print("Would you like to calculate anything else: ")
repeat = int(input("1.Yes \n2.No\n"))


if repeat == 1:
	print("\n------------------------------------------------------------\n")
	for repeat in range(100):
		calc()
else:
	quit()
