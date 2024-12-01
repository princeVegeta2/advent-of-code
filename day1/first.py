class FirstAdvent(object):

    def isSmallest(self, list, number):
        
        for i in list:
            if (isinstance(i, int)):
                if (i < number):
                    return False
        
        return True 

    
    def findDistances(self, list):
        distances = []

        while any(isinstance(item, int) for item in list):
            for i in range(0, len(list)):
                if (isinstance(list[i], int)):
                    if (self.isSmallest(list, list[i])):
                        distances.append(list[i])
                        list[i] = "!"
                
        
        return distances
    
    def findDistanceSum(self, list1, list2):
        mutantList1 = list1[:]
        mutantList2 = list2[:]
        firstDistances = self.findDistances(mutantList1)
        secondDistances = self.findDistances(mutantList2)
        
        sum = 0
        
        for i in range(0, len(firstDistances)):
            sum += abs(firstDistances[i] - secondDistances[i])
        


        return sum
    
    def calculateOccurances(self, list1, list2):
        occuranceList = []
        result = 0
        for i in list1:
            currentCount = 0
            for j in list2:
                if (i == j):
                    currentCount += 1
            occuranceList.append(currentCount)
            currentCount = 0

        for o in range(len(list1)):
            result += occuranceList[o] * list1[o]
        
        return result
    
    def finalResult(self):
        leftList = []
        rightList = []
        globalSum = 0

        with open('input.txt', 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    leftList.append(int(parts[0]))
                    rightList.append(int(parts[1]))

        globalSum = self.findDistanceSum(leftList, rightList)
        globalOccurances = self.calculateOccurances(leftList, rightList)
        return globalSum, globalOccurances
    



    
        



                      


    

firstAdvent = FirstAdvent()
list1 = [3, 4, 2, 1, 3, 3]
list2 = [4, 3, 5, 3, 9, 3]
print(firstAdvent.finalResult())


