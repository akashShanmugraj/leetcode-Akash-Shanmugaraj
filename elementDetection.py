import numpy as np

board = [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
boardArray = np.array(board)
target = input('Enter target element: ')

# Using numpy to find elements in the array
def arraytoList(outArray):
    newArray = []
    for element in outArray:
        newArray.append(list(element))
    return newArray

location = np.where(boardArray == target)
print(arraytoList(location))

# for row in board:
#     for element in row:
#         print(element)
# for row in board:
#     for element in row:
#         index = [board.index(row), row.index(element)]
#         print('Element caught in the iteration is', element, 'at index', index)
#
#         if element == target:
#             print('Element found at', [board.index(row), row.index(element)])