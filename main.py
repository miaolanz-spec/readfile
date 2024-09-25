# Description:
# Describe what this program does such as:
# practice file and dictionaries


# Read a text file and loop through each line of the file and look at each letter in the line to create a dictionary where
# the letters of the alphabet are the keys and the number of times that each letter occurred is the value.
#
# Input parameter: fileName the opening file name, default is speech.txt
# Output value: A dictionary where the letters of the alphabet are the keys and the number of times that each letter occurred is the value.
def readFile(fileName='speech.txt'):
    # Open file
    myDictionary = dict() # init a dictionary
    readFile = open(fileName, 'r') # open a file
    for line in readFile: # loop through each line of the file
        for character in line: # read each letter in the line
            if character.isalpha(): # only the letters of the alphabet
                character = character.lower() # convert to lower case
                if not character in myDictionary: # if the letter doesn't exit in the dictionary
                    myDictionary[character] = 1
                else:
                    myDictionary[character] = myDictionary[character] + 1
    readFile.close()
    # print(myDictionary) # debug
    return myDictionary

# Sort the keys in the dictionary.
#
# Input parameter: myDictionary the dictionary where the letters of the alphabet are the keys and the number of times that each letter occurred is the value.
# Output value: sorted keys
def sortKeys(myDictionary):
    keys = myDictionary.keys();
    sortedKeys = sorted(keys)
    # print(sortedKeys) #debug
    return sortedKeys;

def main():
    myDictionary = readFile("speech.txt")
    sortedKeys = sortKeys(myDictionary)
    print("The frequency of letters are:")
    for sortedKey in sortedKeys:
        print(sortedKey, ":", myDictionary[sortedKey])

main()

