board = [['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

target = input('Enter target element: ')
for row in board:
    for element in row:
        index = [board.index(row), row.index(element)]
        print('Element caught in the iteration is', element, 'at index', index)

        if element == target:
            print('Element found at', [board.index(row), row.index(element)])