import sys
import math

number = int(sys.argv[1])

def is_prime(num):
  if num <= 1:
    return False
  
  prime = True

  for i in range(2, math.ceil(num / 2) + 1):
    if num % i == 0:
      prime = False
  
  return prime

print(is_prime(number))