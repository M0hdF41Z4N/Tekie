def checkPrime(num):
  if num<2:
    return False
  if num == 2:
    return True
  for i in range(3,num//2):
    if num%i == 0:
      return False
  return True
#Driver Code
number = int(input())
print(checkPrime(number))
