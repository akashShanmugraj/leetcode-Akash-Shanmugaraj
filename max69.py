# solved on 7th November 2022
# find this problem on https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        numList = list(str(num))
        numList[numList.index('6')] = '9'
        finalInt = int(''.join(numList))
        print(finalInt)
        return finalInt
