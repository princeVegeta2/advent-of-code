import re

class FourthAdvent(object):

    def getInput(self, inputFile):
        xmasList = []

        with open(inputFile, 'r') as file:
            for line in file:
                char_list = list(line.strip())
                xmasList.append(char_list)
        
        return xmasList
    
    def isMas(self, xmasList, i, j):
        rows = len(xmasList)
        cols = len(xmasList[0])

        if xmasList[i][j] != 'A':
            return False
        if i - 1 < 0 or i + 1 >= rows or j - 1 < 0 or j + 1 >= cols:
            return False 
        
        mases = 0

        primary = xmasList[i - 1][j - 1] + xmasList[i][j] + xmasList[i + 1][j + 1]
        if primary == 'MAS' or primary == 'SAM':
            mases += 1
        
        secondary = xmasList[i - 1][j + 1] + xmasList[j][j] + xmasList[i + 1][j - 1]
        if secondary == 'MAS' or secondary == 'SAM':
            mases += 1
        
        return mases == 2

                        


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

        # Process primary diagonals 
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

        # Process anti-diagonals 
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

# MAS
rows = len(inputList)
cols = len(inputList[0])
occurances = 0
for i in range(rows):
    for j in range(cols):
        if fourthAdvent.isMas(inputList, i, j):
            occurances += 1
print("MAS's: ", occurances)
