class SecondAdvent(object):

    def isSafe(self, inputList):
        # Only increasing or only decreasing
        # Minimum by 1 
        # Maximum by 3

        increasing = inputList[0] < inputList[1]
        decreasing = inputList[0] > inputList[1]
        dampened = 0

        for i in range(len(inputList)):
            if i != len(inputList) - 1:
                if inputList[i] < inputList[i + 1] and increasing:
                    if inputList[i + 1] - inputList[i] >= 1 and inputList[i + 1] - inputList[i] <= 3:
                        continue
                    elif dampened <= 1:
                        dampened += 1
                        continue
                    else:
                        return False 
                elif inputList[i] > inputList[i + 1] and decreasing:
                    if inputList[i] - inputList[i + 1] >= 1 and inputList[i] - inputList[i + 1] <= 3 and dampened == 0:
                        continue
                    elif dampened <= 1:
                        dampened += 1
                        continue 
                    else:
                        return False 
                else:
                    return False


        return True

    def getInput(self, inputFileName):
        outputLists = []
        with open(inputFileName, 'r') as file:
            for line in file:
                currentList = [int(number) for number in line.strip().split()]
                outputLists.append(currentList)
        
        return outputLists
                

safeLists = 0
secondAdvent = SecondAdvent()
inputLists = secondAdvent.getInput('input.txt')
for i in inputLists:
    if secondAdvent.isSafe(i):
        safeLists += 1


print("Safe lists: ", safeLists)
