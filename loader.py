def loader(readfile, writefile):
    punctuation = [",", ";", ":", "-", ".", "\n"]
    aposthrope = ["'s", "'d"]
    word = []
    current_word = ""

    with open(readfile, "r") as doc1:
        for line in doc1:
            line = line.lower()
            new_line = ""
            for letters in line:
                if letters in punctuation:
                    letters = " "
                new_line += letters

            for letters in new_line:
                if letters != " ":
                    current_word += letters
                else:
                    word.append(current_word)
                    current_word = ""

            if current_word != "":
                word.append(current_word)
            current_word = ""

    c = 0

    for current_word in word:
        for ap in aposthrope:
            if current_word.endswith(ap):
                current_word = current_word[:-len(ap)]
        word[c] = current_word
        c += 1

    with open(writefile, "w") as clean:
        for current_word in word:
            if current_word != "":
                clean.write(current_word + "\n")
