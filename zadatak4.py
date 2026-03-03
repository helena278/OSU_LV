wordsDict={}

file=open('song.txt')
for line in file:
    line = line.rstrip()
    words = line.split()
    for word in words:
        word=word.rstrip(',')
        if word in wordsDict:
            wordsDict[word]+=1

        else:
            wordsDict[word]=1
file.close()

print(wordsDict)
count=0

print("Unique words:")
for key in wordsDict:
    if wordsDict[key]==1:
        print(key)
        count+=1

print(f"Number of unique words: {count}")