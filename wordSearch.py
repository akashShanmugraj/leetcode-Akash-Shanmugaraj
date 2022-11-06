#https://leetcode.com/problems/word-search-ii/
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
#https://leetcode.com/problems/word-search-ii/discuss/59780/Python-dfs-solution-(directly-use-Trie)/61810

import numpy as np

board = [["a","b"],["c","d"]]
words = ["abcb"]
foundWords = []

def tryException(x,y):
    try:
        return [board[x][y],x,y]
    except IndexError:
        return None
def findNeighbours(x,y):
    return [tryException(x-1,y), tryException(x+1, y),tryException(x,y-1), tryException(x,y+1)]



def removeFinding(output, target):
    try:
        for out in output:
            if out is not None:
                if out[1] != target:
                    output.remove(out)
        return output
    except IndexError:
        return None

def main(index,coordinates, word, pathUpdater):
    x,y = coordinates
    if index >= len(word)-1:
        if pathUpdater == word:
            foundWords.append(word)
            return True
        else:
            return False
    else:
        neighbours = findNeighbours(x, y)
        for neighbour in neighbours:
            if neighbour != None:
                if neighbour[0] == word[index+1]:
                    pathUpdater += neighbour[0]
                    main(index+1, [neighbour[1], neighbour[2]], word, pathUpdater)

        index += 1


def coordinatesfromArray(outArray):
    newArray = []
    xCoords, yCoords = outArray
    for num in range(len(xCoords)):
        newArray.append([xCoords[num], yCoords[num]])

    return newArray

def findElementArray():
    for word in words:
        path = word[0]
        boardArray = np.array(board)
        locate = coordinatesfromArray(np.where(boardArray == word[0]))
        for coord in locate:
            main(0, coord, word, path)
    return foundWords

# Usage
print(findElementArray())

