print("Enter the Numbers seperated by space.")
numList = list(map(int,input().split(" "))) # To take input as List of Integer numbers
numList.sort() # To Sort the list of numbers.
print(numList[-2])
