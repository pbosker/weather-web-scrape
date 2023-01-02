word_set = {}
letter = "?"
occurance = 0

def sortString(str):
    return ''.join(sorted(str))

words = "Heavy rainfall can cause normally dry washes and riverbeds to become raging torrents in a very short amount of time and it only takes as little as 12 inches of moving water to move a vehicle, San Bernardino County Fire Department officials said. Never cross a road that you can’t see due to it being covered by water, remember, ‘Turn Around, Don’t Drown.’ supercalifragilisticexpialidocious"
word_set = words.split(" ")

for word in word_set:
    for i in sortString(word):
        if str(i) == letter:
            occurance += 1
            hold_letter = letter
            hold_word = word
        else:
            if occurance > 1:
                print("There are " + str(occurance) + " " + hold_letter.upper() + "'s in the word " + hold_word)
            occurance = 1
        letter = str(i)
