#This is using backtracking -> N S, 2^N T
# class Some:
#     def __init__(self, n):
#         self.arr = [None] * n
#         self.n = n

#     def binOfN(self, i=0):
#         if i == self.n:


#     def addToList(self, arr):
 
# Function to print the output
def printTheArray(arr):
    return ''.join([str(i) for i in arr])
 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        lis.add(printTheArray(arr)) 
        return
     
    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)
 
# Driver Code
if __name__ == "__main__":
 
    n = int(input("Enter the number"))
    lis = set()
    arr = [None] * n
    generateAllBinaryStrings(n, arr, 0)
    print(lis)
       
