length = 0
lengsta = ''

with open("words.txt") as words:
    
    for word in words:
        word = word.replace("\n", "")
        if len(word) > length:
            length = len(word)
            lengsta = word

print("Longest word is '{}' of length {}".format(lengsta, length))