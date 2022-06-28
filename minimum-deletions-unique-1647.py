import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        dic,sett,count = collections.Counter(s),set(),0
        for i in dic.values():
            while i > 0 and i in sett:
                i-=1
                count+=1
            sett.add(i)
        return count

# Instead of counters we can also you dictionary one liner 
# dict[n] = dict.get(n,0)+1 but they are the same. The idea behind 
# is that we keep a record of the amount of frequencies in a hashmap 
# (set). and if that frequency is already present, then we reduce the 
# value of that frequency variable in the loop by 1 and also add the 
# operation count by 1. This process repeats untill we get a value that 
# is not present in the hashmap or untill the value is greater that 0 
# (as the occurance cant be 0 or negative -  if it was it would'nt
#  in the record of frequencies). Once its not present in the map we 
# add it there and continue the iteration to the next 
# frequency of a different character