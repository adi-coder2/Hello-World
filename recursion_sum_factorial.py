#Sum of first n natural number
def sum(n):
	if n == 0:
		return 0
	else:
		return (n + sum(n - 1))


#Factorial

def factorial(n):
	if n == 0:
		return 1
	else:
		return (n * factorial(n - 1))



#Choice to select for User
print("What would you like to do:")
print("1.Find the sum of first n natural number:")
print("2.Find the factorial of a number:")
choice = int(input("Enter Your Choice:	"))



#Taking User Input
a = int(input("Enter your number: "))



#Performing Operation Based on User Input
if choice == 1:
	print(f"The sum from 1 to {a} is {sum(a)}")
elif choice == 2:
	print(f"The factorial of {a} is {factorial(a)}")
else:
	print("Invalid operation")  
