with open("words.txt") as words:
    with open("sentences.txt", 'w') as sentence:
        for word in words:
            word = word.replace(" ", "")
            word = word.replace("\n", "")
            if word == '.':
                print(word)                
                sentence.write(f'{word}\n')
            else:
                print(word, end=' ')
                sentence.write(f'{word} ')


