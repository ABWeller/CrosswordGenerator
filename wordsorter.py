def CreateWordLengthDict(filepath):
    """
    Reorganizes a txt file containing a word set into a dictionary with the word's length as its key
    :param filepath: (.txt) directory of the file containing the desired word set, one word per line
    :return: dict: a dictionary of the words in filepath file, sorted by their length as the key: {wordlength: [word, word, etc.]}
    """

    orderedwords = {}
    with open(filepath, "r") as file:
        for word in file:
            rawword = word.strip("\n")
            length = len(rawword)
            if length in orderedwords:
                orderedwords[length].append(rawword)
            else:
                orderedwords[length] = [rawword]

    return orderedwords
