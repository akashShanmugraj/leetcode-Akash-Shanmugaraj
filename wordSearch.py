#https://leetcode.com/problems/word-search-ii/
# Given a 2D board and a list of words from the dictionary, find all words in the board.
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# Example:
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
# You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
# If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
#https://leetcode.com/problems/word-search-ii/discuss/59780/Python-dfs-solution-(directly-use-Trie)/61810

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
foundWord = ''
pathList = []
# pathUpdater = ''
# processCount = 0

def findNeighbours(x,y,mode):
    try:
        if x != 0:
            if mode=='up':
                return [board[x-1][y],x-1,y]
        elif y != 0:
            if mode=='left':
                return [board[x][y-1],x,y-1]
        if mode == 'down':
            return [board[x + 1][y], x + 1, y]
        elif mode=='right':
            return [board[x][y+1],x,y+1]
        elif mode == 'all':
            return [board[x-1][y],board[x+1][y],board[x][y-1],board[x][y+1]]


    except IndexError:
        return None

def removeFinding(output, target):
    try:
        for out in output:
            if out != None:
                if out[1] != target:
                    output.remove(out)
        return output
    except IndexError:
        return None

def main(index,x,y, word, pathUpdater):
    # print('Current path is ',pathUpdater)
    if index >= len(word)-1:
        print('Found word is ',word)
        print('\n\n')
        return False
    else:
        print('word now is', word, 'path is', pathUpdater)

        neighbours = [findNeighbours(x,y,'up'), findNeighbours(x,y,'down'), findNeighbours(x,y,'left'), findNeighbours(x,y,'right')]
        print('Neighbours in the direction up, down, left and right respectively are', neighbours)
        for neighbour in neighbours:
            if neighbour != None:
                if neighbour[0] == word[index+1]:
                    pathUpdater += neighbour[0]
                    print(neighbour[0], 'with nearby index')
                    main(index+1, neighbour[1], neighbour[2], word, pathUpdater)
                elif neighbour[0] != word[index+1]:
                    print(f'not matching ({board[x][y]})')
                    # board[x][y] = '$'

        index += 1

def findElement():
    for row in board:
        for element in row:
            for word in words:
                if element == word[0]:
                    path = element
                    main(0, board.index(row), row.index(element),word, path)

print(findElement())

