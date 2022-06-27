class Solution:
    def minPartitions(self, n: str) -> int:
        return max(n)
# The theory is a deci-binary number is a decimal whose digits
# can either be 1 or 0. So to represent 32 in deci-binary 
# we use 10, 11, 11. Now at any digit to increase we can 
# do it by only one at a time because we use either 0 or 1 so
#  32 can also be written as => 3 2
#                               1 1
#                               1 1
#                               1 0
# Incase of 82734, the biggest number being 8, we would need atleast
# 8 numbers (8*1) as there are no carry overs. So its safe to say that 
# no matter how big the number it can be represented using len(n) 
# deci-binaries where n is the number. Also max number of deci-binary numbers to represent
# any number will not be more that 9.