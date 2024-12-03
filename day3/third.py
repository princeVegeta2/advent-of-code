import re

class ThirdAdvent:
    def getInput(self, inputFileName):
        """
        Reads the content of the input file and returns it as a single string.
        """
        with open(inputFileName, 'r') as file:
            return ''.join(line.strip() for line in file)
    
    def formatString(self, inputString):
        """
        Formats the input string to extract valid 'mul(number,number)' and 'do()' and 'don't()' patterns.
        """

        pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
        matches = re.findall(pattern, inputString)
        
        return matches

    def calculateSum(self, substrings):
        total_sum = 0
        skip = False

        for substring in substrings:
            if substring == "don't()":
                skip = True
            elif substring == "do()":
                skip = False
            elif not skip:
                numbers = re.findall(r"\d+", substring)
                num1, num2 = map(int, numbers)
                total_sum += num1 * num2
        
        return total_sum

# Create an instance of ThirdAdvent
thirdAdvent = ThirdAdvent()

# Read the input file and process it
inputString = thirdAdvent.getInput('input.txt')
formattedSubstrings = thirdAdvent.formatString(inputString)

# Calculate the sum of the multiplications
totalSum = thirdAdvent.calculateSum(formattedSubstrings)

# Print the results
print("Do, Dont and muls: ", formattedSubstrings)
print("Total Sum of Multiplications:", totalSum)
