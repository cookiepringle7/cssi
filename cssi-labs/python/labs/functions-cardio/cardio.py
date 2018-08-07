def longest_word(word1,word2,word3):

    if len(word1) > len(word2) and len(word1) > len(word3):
        print word1
    elif len(word2) > len(word1) and len(word2) > len(word3):
        print word2
    else:
        print word3
longest_word("nameon", "boy", "girls")
