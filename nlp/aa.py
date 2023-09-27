import math

def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def main():
  """Checks if the given number is prime and prints the square root of the number if it is prime."""
  num = int(input("Enter a number: "))
  if is_prime(num):
    print(math.sqrt(num))
  else:
    print(f"{num} is not a prime number.")

if __name__ == "__main__":
  main()
  