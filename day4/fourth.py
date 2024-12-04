import re

class FourthAdvent(object):

    def getInput(self, inputFile):
        xmasList = []

        with open(inputFile, 'r') as file:
            for line in file:
                char_list = list(line.strip())
                xmasList.append(char_list)
        
        return xmasList
    
    def findMas(self, xmasList):
        occurences = 0
        rows = len(xmasList)
        cols = len(xmasList[0]) if rows > 0 else 0

        for i in range(rows):
            for j in range(cols):
                if xmasList[i][j] == 'A':
                    if (
                        (0 <= i - 1 < rows and 0 <= j - 1 < cols and 0 <= i + 1 < rows and 0 <= j + 1 < cols) and
                        (
                            (xmasList[i - 1][j - 1] == 'M' and xmasList[i + 1][j + 1] == 'S') or 
                            (xmasList[i - 1][j - 1] == 'S' and xmasList[i + 1][j + 1] == 'M')
                        )
                    ):
                        occurences += 1
                    
                    if (
                        (0 <= i - 1 < rows and 0 <= j + 1 < cols and 0 <= i + 1 < rows and 0 <= j - 1 < cols) and
                        (
                            (xmasList[i - 1][j + 1] == 'M' and xmasList[i + 1][j - 1] == 'S') or
                            (xmasList[i - 1][j + 1] == 'S' and xmasList[i + 1][j - 1] == 'M')
                        )
                    ):
                        occurences += 1
        
        return occurences
                        


    def findLists(self, xmasList):
        occurances = 0
        pattern = r'(?=(XMAS))'  

        rows = len(xmasList)
        cols = len(xmasList[0])

        # Process horizontal lines
        for row in xmasList:
            string = ''.join(row)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        # Process vertical lines
        for col in range(cols):
            col_list = [xmasList[row][col] for row in range(rows)]
            string = ''.join(col_list)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        # Process primary diagonals (top-left to bottom-right)
        for col in range(cols):
            diag_list = []
            r, c = 0, col
            while r < rows and c < cols:
                diag_list.append(xmasList[r][c])
                r += 1
                c += 1
            string = ''.join(diag_list)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        for row in range(1, rows):
            diag_list = []
            r, c = row, 0
            while r < rows and c < cols:
                diag_list.append(xmasList[r][c])
                r += 1
                c += 1
            string = ''.join(diag_list)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        # Process anti-diagonals (top-right to bottom-left)
        for col in range(cols - 1, -1, -1):
            diag_list = []
            r, c = 0, col
            while r < rows and c >= 0:
                diag_list.append(xmasList[r][c])
                r += 1
                c -= 1
            string = ''.join(diag_list)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        for row in range(1, rows):
            diag_list = []
            r, c = row, cols - 1
            while r < rows and c >= 0:
                diag_list.append(xmasList[r][c])
                r += 1
                c -= 1
            string = ''.join(diag_list)
            occurances += len(re.findall(pattern, string))
            # Reversed
            occurances += len(re.findall(pattern, string[::-1]))

        return occurances

# Usage
fourthAdvent = FourthAdvent()
inputList = fourthAdvent.getInput('input.txt')
occurances = fourthAdvent.findLists(inputList)
print("Occurrences:", occurances)

