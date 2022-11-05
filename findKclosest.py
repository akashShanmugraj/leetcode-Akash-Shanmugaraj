# find this question at https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        arr = arr[:k]
        finalList = []
        proximityValues = []
        for element in arr:
            formulaOutput = abs(element-x)
            proximityValues.append(formulaOutput)
            proxydup = proximityValues.copy()
        print(arr,proximityValues)
        for interation in range(k):
            localMinimum = min(proximityValues)
            localMinimumIndex = proximityValues.index(localMinimum)
            
            finalList.append(arr[localMinimumIndex])
            print(localMinimum, proximityValues)
            proximityValues[localMinimumIndex] = 1000000

        finalList.sort()
        print('finalList is ', finalList)        
        return finalList
Solution.findClosestElements(Solution,[1,2,3,4,6,7,9], 3, 5)