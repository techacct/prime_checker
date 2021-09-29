# define function
def prime_checker(number):
  is_prime = True

  for i in range(2, number):
    # check if number is divisible by all numbers before number
    if number % i == 0:
      is_prime = False
  if is_prime:
    print(f'The number {number} is a prime number')
  else:
    print(f'The number {number} is not a prime number')
  
# receive input from user
n = int(input("Check this number: "))
prime_checker(number=n)





















