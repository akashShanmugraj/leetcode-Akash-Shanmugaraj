class Solution:
    def makeGood(self, s: str) -> str:
        compareList = []
        mainList = list(s)

        for letter in mainList:
            if compareList == []:
                compareList.append(letter)
            else:
                if letter == compareList[-1].swapcase():
                    compareList.pop()
                else:
                    compareList.append(letter)
        
        return ''.join(compareList)

print(Solution.makeGood(Solution, 'LlEEeetcode'))