try:
    with open('./week6/input.txt') as source_file, open('./week6/output.txt', 'w') as destination_file:
        list_of_words = []
        for line in source_file:
            for word in line.split():
                list_of_words.append(word.lower())
        list_of_words.sort()

        for word in list_of_words:
            destination_file.write(word)
            destination_file.write(" ")
except FileNotFoundError:
    print('The source file and/or destination file is not present')
