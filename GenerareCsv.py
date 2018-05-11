import csv

text = open("Text.txt", "r")

text = text.read()

nrDots = 0

dotList = []

for singleTuple in enumerate(text):
    if singleTuple[1] == ".":
        dotList.append(singleTuple[0])
nrDots = len(dotList)
print(nrDots)
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

urmEnter = []
for letter in wordAfterPoint:
    if letter[0] == "\n":
        urmEnter.append("T")
    else:
        urmEnter.append("F")

precPresc = []
inAbr = []
for word in wordBeforePoint:
    if word[0].isupper and (word[1] == "." or word[1] == " "):
        inAbr.append("T")
    else:
        inAbr.append("F")

print inAbr
print urmEnter
print wordBeforePoint
print wordAfterPoint

with open('data.csv', 'wb') as csvfile:
    fieldnames = ['inAbr', 'urmEnter']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for index in range(0, nrDots):
        writer.writerow({'inAbr': inAbr[index], 'urmEnter': urmEnter[index]})

