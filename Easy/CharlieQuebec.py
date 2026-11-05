codeWords = {
    "a": "Alpha",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliet",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "Xray",
    "y": "Yankee",
    "z": "Zulu",
}

testCases = int(input())

for i in range(testCases if testCases >= 1 else 1):
    casespart2 = int(input())
    for _ in range(casespart2 if casespart2 >= 1 else 1):
        words = input()
        codedWord = ""
        for p, l in enumerate(words):
            if l.lower() in codeWords.keys():
                newLetter = codeWords[l.lower()]
                if (p < (len(words)-1)) and (words[p+1] != " "):
                    newLetter += "-"
                codedWord += newLetter
            elif l == " ":
                codedWord += " "
        print(codedWord)