class Solution:
    def removeDuplicates(self, string: str) -> str:
        mainList = list(string)
        compareList = []
        for character in mainList:
            lastChar = compareList and compareList[-1]
            if character == lastChar:
                compareList.pop()
            else:
                compareList.append(character)
        return ''.join(compareList)