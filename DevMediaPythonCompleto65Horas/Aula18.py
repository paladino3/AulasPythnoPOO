#Dictionary

print('Test Dictionart')
"""
myDictionaryHeight = {'Wesley':1.76, 'Silva':1.92 , 'Dirceu':1.65} #{dicionarios, com chaves}

print('All height: ',myDictionaryHeight)

print('\nSilva current height: ',myDictionaryHeight['Silva'])
myDictionaryHeight['Silva'] = 1.78
print('\nSilva NEW height: ',myDictionaryHeight['Silva'])


myDictionaryHeight['marcos'] = 1.63

print('Sictionary after insert: ',myDictionaryHeight)
del myDictionaryHeight['Wesley']
print('All height: ',myDictionaryHeight)
"""

def histogram(text):
    myDictionary = dict()
    for c in text:
        if c not in myDictionary:
            myDictionary[c]=1
        else:
            myDictionary[c]+=1
    return myDictionary
def print_histogram(dictionary):
    for c in dictionary:
        print(c,dictionary[c])

result = histogram('Devimedia is a great company to learn programing')
print_histogram(result)