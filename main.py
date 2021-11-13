import random

inputFile = open("input", "r")

inputFileContent = inputFile.readlines()


letterList = []
followingLetterList = []

#add letters, lowercase, I'll compare case insensitive
for x in range(97,122+1):
    letterList.append(chr(x))

    #append an empty list in the following letters list
    followingLetterList.append([])

#print(letterList)
maxLength = 0

for x in inputFileContent:

    if len(x) > maxLength:
        maxLength = len(x)

    letterIndex = 0
    for index in range(0, len(x)-1):
        #-1 because the last letter has no letter after it
        if x[index] == ' ':
            pass
        #ignore spaces
        else:
            #assume it's letter, add it's next to the appropriate list

            letterIndex = letterList.index((x[index]).lower())  #if it's in the list, get it's index
            if x[index+1] == '\n' or x[index+1] == ' ':
                #ignore
                pass
            else:
                followingLetterList[letterIndex].append(x[index+1])

#now that we've collected the data, now let's use it make names

#generate a random number, get a letter that follows it, if none exists pick a random one
newRandom = random.randint(0,25)

output = ""
output += letterList[newRandom]
minLength = 5
randomLength = random.randint(minLength, maxLength)

for x in range(randomLength):
    lastLetter = output[-1]

    if lastLetter == '\n':
        pass
    #ignore
    else:

        indexToGet = letterList.index(lastLetter)
        listOfPossibleLetters = followingLetterList[indexToGet]



        if len(listOfPossibleLetters) == 0:
            #pick a random letter
            newRandom = random.randint(0, 25)
            output += letterList[newRandom]
        else:
            letterPicker = random.randint(0, len(listOfPossibleLetters)-1)


            output += listOfPossibleLetters[letterPicker]

print(output)

