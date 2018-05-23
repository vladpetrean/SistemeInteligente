import csv

from cuvintePrescurtate import wordTreeLetters, wordTwoLetters
from strings import is_lower
from PrenumeRomanesti import obtainPrenume
from NumeRomanesti import obtainNume

try:
    text = open("Text.txt", "r")
except ValueError:
    print ValueError

listaPrenume = obtainPrenume()
listaNume = obtainNume()

text = text.read()
nrDots = 0
dotList = []

for singleTuple in enumerate(text):
    if singleTuple[1] == ".":
        dotList.append(singleTuple[0])

nrDots = len(dotList)

entireWordAfterPoint = []
spaceListIndex = []
wordBeforePoint = []
wordAfterPoint = []
auxiliarString = ""

word = ""
for index in dotList:
    for singleTuple in enumerate(text):
        auxiliarString = auxiliarString + singleTuple[1]
        if index == singleTuple[0]:
            word = ""
            for character in reversed(auxiliarString):
                if character != " ":
                    word = word + character
                else:
                    reverseWord = ""
                    for letter in reversed(word):
                        reverseWord = reverseWord + letter
                    wordBeforePoint.append(reverseWord)
                    auxiliarString = ""
                    break

            word = ""
            checkNextLetter = False
            for character in text[index + 1:]:
                if checkNextLetter:
                    word = word + character
                    wordAfterPoint.append(word)
                    word = ""
                    break
                if character != " " and character != "\n":
                    word = word + character
                else:
                    word = word + character
                    checkNextLetter = True
            checkWord = 0
            for character in text[index + 1:]:

                if checkWord == 2:
                    entireWordAfterPoint.append(word[:-1])
                    word = ""
                    break
                if character != " " and character != "\n":
                    word = word + character
                else:
                    word = word + character
                    checkWord = checkWord + 1

entireWordAfterPointAux = []

for word in entireWordAfterPoint:
    if word.endswith('.'):
        word = word[:-1]
        entireWordAfterPointAux.append(word)
    else:
        entireWordAfterPointAux.append(word)

entireWordAfterPoint = entireWordAfterPointAux
if wordAfterPoint[-1] != "\n":
    wordAfterPoint.append(" ")

urmEnter = []
for letter in wordAfterPoint:
    if letter[0] == "\n":
        urmEnter.append("T")
    else:
        urmEnter.append("F")

inAbr = []

for word in wordBeforePoint:
    if word[0].isupper and word[1] == ".":
        inAbr.append("T")
    else:
        inAbr.append("F")

precPresc = []

for word in wordBeforePoint:
    word = word[:-1]
    if is_lower(word) and word.isalpha():
        if len(word) == 2:
            if word in wordTwoLetters:
                precPresc.append("F")
            else:
                precPresc.append("T")
        elif len(word) == 3:
            if word in wordTreeLetters:
                precPresc.append("F")
            else:
                precPresc.append("T")
        else:
            precPresc.append("F")

    else:
        precPresc.append("F")

print("Introduceti numarul corespunzator punctului aflat la final de proprozitie, dupa ce termianti inserati 0 ")
endPoints = []
auxiliara = 1

while auxiliara != 0:
    inputData = input("Numar punct final de propozitie: ")
    if inputData == 0:
        auxiliara = 0
    else:
        endPoints.append(inputData)

classList = []
for index in range(0, nrDots):
    classList.append("F")

for index in enumerate(endPoints):
    classList[index[1] - 1] = "T"

urmSpUpCharNoName = []

# ------------------------------ Verificare + Redactare CSV ------------------------------

print "UrmSpUpCharNoName"

print "Class "
print classList

print "Prec presc"
print precPresc

print "In ABR "
print inAbr

print "urm enter"
print urmEnter

print"Word Before point"
print wordBeforePoint

print"Word After point"
print entireWordAfterPoint

with open('data.csv', 'wb') as csvfile:
    fieldnames = ['inAbr', 'urmEnter', "precPresc", "class"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for index in range(0, nrDots):
        writer.writerow({'urmEnter': urmEnter[index], 'precPresc': precPresc[index], 'inAbr': inAbr[index],
                         "class": classList[index]})
