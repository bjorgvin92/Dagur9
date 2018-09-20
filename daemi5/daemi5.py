with open("words.txt") as words:
    with open("sentences.txt", 'w') as sentence:
        for word in words:
            word = word.replace(" ", "")
            word = word.replace("\n", "")
            if word[-1] == '.':
                print(word)                
                sentence.write(word)
                word = '\n'
                sentence.write(word)
            else:
                print(word, end=' ')
                sentence.write(word)
                word = ' '
                sentence.write(word)

