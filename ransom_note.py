def checkMagazine(magazine, note):
    magazineArr = magazine.split()
    noteArr = note.split()
    magazineDict = {}
    for word in magazineArr:
        if word not in magazineDict:
            magazineDict[word] = 1
        else:
            magazineDict[word] += 1
    for word in noteArr:
        if word in magazineDict:
            if magazineDict[word] > 0:
                magazineDict[word] -= 1
            else:
                return False
        else:
            return False
    return True


magazine = "give me one grand today night"
note = "give one grand today"
print(checkMagazine(magazine, note))
