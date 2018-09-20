with open("test.txt") as f:
    prentari = f.read()
    prentari = prentari.replace(" ", "")
    prentari = prentari.replace("\n", "")

    print(prentari)