import random
from CharsSplittingShit import *
from TimeShit import *

varFile = open('vars.txt', 'r')
numOfNames = int(varFile.readline())
lenOfNames = int(varFile.readline())
namesFile = open(varFile.readline(), 'a')
varFile.close()

charChoice = ''
finalString = ''
namesFile.write("\n___Date of Generation: " + now + " ___")
for z in range(0, numOfNames):
    for i in range(0, lenOfNames):
        charChoice = random.choice(splitChars)
        finalString += charChoice
        if i == lenOfNames-1:
            i = 0
            namesFile.write("\n"+finalString)
            finalString = ''
namesFile.write("\n___MCUsernameGen by JamesTheGeek___")
namesFile.close()
