# https://leetcode.com/problems/reverse-integer/description/

# from struct import pack, error

class Solution:
    def reverse(self, x: int) -> int:
        modString = str(abs(x))[::-1]
        finalInt = 0
        if x < 0:
            finalInt =  -int(modString)
        else:
            finalInt = int(modString)

        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1
        
        if finalInt > ma or finalInt < mi:
            return 0
        return finalInt

    # def test_32bit(n):
    #     try:
    #             pack("i", n)
    #     except error:
    #             return False
    #     return True

# Find out why below x is not considered as a 32 bit in the original solution 
print(Solution.reverse(Solution, 1534236469))