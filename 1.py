while True:

    print("Enter 'a' - to sort words alphabetically:")
    print("Enter 'b' - count each letter in the text:")
    print("Enter '0' - to exit:")

    user = input()
    text = input("Enter your text:")
    if user == 'a':
        words = (sorted(text.split(), key=str.lower))
        uniqueWords = set()
        for word in words:
            if word not in uniqueWords:
                uniqueWords.add(word)
                if len(word.strip()) > 2:
                    print(word)

        print("program 'a' finished \n")

    if user == 'b':
        print("Start counting \n")

        symbols = dict()

        for i in str.lower(text):
            if i == ' ':
                continue

            if i in symbols:
                symbols[i] += 1
            else:
                symbols[i] = 1

        for character in symbols:
            print("Letter ", character, " number = ", symbols[character])

        print("program 'b' finished \n")

    if user == '0':
        print("Program finished")
        break