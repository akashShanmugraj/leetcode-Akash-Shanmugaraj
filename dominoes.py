
class Solution:
    def compareposition(self, cursor,source):
        try:
            if source[cursor] == source[cursor+1]:
                return False
            else:
                return True
        except IndexError:
            return None
    def pushDominoes(self, dominoes: str):
        finalString = ''
        if dominoes == '.':
            print('. was returned')
            return '.'
        dominoes += '  '
        stringLength = len(dominoes)
        finalState = list(dominoes)
        
        for pieceindex in range(stringLength):
            element = finalState[pieceindex]
            print('The element caught in the iteration was', element)
            if element != ' ':
                print('The element {', element,'} was passed here, indicating that it was not a blank space')
                if element == '.' and finalState[1] == 'L' :
                    print('The incoming element is a "." at index 0, the next element at index 1 has L')
                    print('finalState variable was', finalState)
                    finalState[0] = finalState[1]
                    print('and now is', finalState)
                    print('\n')
                elif element == '.' and finalState[pieceindex-1] == 'R':
                    print(f'The incoming element is a "." found at {stringLength-3} and the negative 4th element is an R')
                    print('finalState variable was', finalState)
                    finalState[-3] = finalState[-4]
                    print('finalState variable is now', finalState)

                else:
                    print(f'The element caught in the iteration was neither a "." at position 0 or {stringLength-3} having a L or R in their adjacent indices respectively')
                    print('finalState variable was', finalState)
                    if element == 'L':
                        print('The element is found to be an L in the middle of the string')
                        if finalState[pieceindex-2] in ['L','.']:
                            print('and the element one before was not a "R" to stop the movement')
                            finalState[pieceindex-1] = "L"
                            if finalState[piece ]
                        elif finalState[pieceindex-2] == 'R':
                            print('and the element one before was a "R" to stop the movement')
                            finalState[pieceindex-1] = "."

                    elif element == 'R':
                        print('The element is found to be an R in the middle of the string')
                        if finalState[pieceindex+2] in ['R', '.']:
                            print('and the element one after was not a "L" to stop the movement')
                            finalState[pieceindex+1] = 'R' 
                        elif finalState[pieceindex+2] == 'R':
                            print('and the element one after was a "L" to stop the movement')
                            finalState[pieceindex+1] = "."
                    print('finalState variable is', finalState)
                
                print('\n\n')
                    
            # print(element, 'element passed')

        finalString = finalString.join(finalState).strip()
        print(finalString)
        return finalString
Solution.pushDominoes(Solution ,"..L")


