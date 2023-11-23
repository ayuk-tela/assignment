
# Initialize a list with 5 integers of your choice
my_list = [1, 2, 3, 4, 5]

# Enter an integer
user_input = int(input("Enter an integer: "))

# Iterate through the list using a for loop
for num in my_list:
    if num == user_input:
        # Save the entry and interrupt the loop
        print("Entry found in the list!")
        break
else:
    # Display a message if the loop completes successfully
    print("Entry not found in the list.")

# Enter another positive integer
user_input = int(input("Enter another positive integer: "))

# Write a while loop to determine if the integer is prime
is_prime = True
divisor = 2

while divisor < user_input:
    if user_input % divisor == 0:
        # Display the first divisor found and interrupt the loop
        print(f"{user_input} is not a prime number. First divisor found: {divisor}")
        is_prime = False
        break
    divisor += 1
else:
    # Display the number if it is prime
    if is_prime:
        print(f"{user_input} is a prime number.")
