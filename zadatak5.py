hamWordCount =[]
spamWordCount = []
exCount=0
file = open('SMSSpamCollection.txt')

for line in file:
    line = line.rstrip()
    words =line.split()
    if words[0]=="ham":
        hamWordCount.append(len(words)-1)
    else:
        spamWordCount.append(len(words)-1)
        if words[-1].endswith('!'):
            exCount+=1

file.close()

print(f"Prosjecan broj rijeci u ham porukama:{int(sum(hamWordCount)/len(hamWordCount))}")
print(f"Prosjecan broj rijeci u spam porukama:{int(sum(spamWordCount)/len(spamWordCount))}")
print(f"Broj spam poruka koje zavrsavaju usklicnikom:{exCount}")
