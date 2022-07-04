class Solution:
    def convert(self, s: str, numRows: int) -> str:
        layers,pointer,switch = ['']*numRows,0,0
        if numRows == 1 or numRows >= len(s): return s
        for i in s:
            layers[pointer]+=i
            if pointer == 0: switch = 1
            elif pointer == numRows - 1: switch = -1
            pointer+=switch
        return "".join(layers)

# The logic is behind knowing the time to switch the order in which the
# letters are appended. And the switch happens once it index reaches the
# length of rows or 0. Since we can define the as many numbers of conditions 
# for adding into the index we use this command add/sub operator whose value 
# acts as the switch
            