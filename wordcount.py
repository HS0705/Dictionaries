# put your code here.

def word_count(filename):
    """Return the word counts in the file"""

    words_file = open(filename)
    words_dict = {}

    # # iterating all the lines in the file
    for line in words_file:
        line = line.strip()
        words = line.split()
        #iterating all the words in line
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1
    return words_dict

    filename.close()
print(word_count("test.txt"))
