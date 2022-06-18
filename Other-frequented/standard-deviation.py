from math import sqrt
sample = [int(input()) for _ in range(int(input("Enter the sample size")))]
mean,numerator = sum(sample)/len(sample),0
for num in sample: numerator += (num - mean)**2
print(sqrt(numerator/len(sample)),mean)