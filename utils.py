import string
from nltk import Text, word_tokenize

sp = string.punctuation + '``' + '...' + "--" + "''"

def count_words():
    length_dict = {}

    for i in range(1, 8):
        textfile = open('corpus/hp' + str(i) + '.txt').read()
        tokenized = word_tokenize(textfile)
        tokenized = [t for t in tokenized if t not in sp and t != "'s"]
        length_dict["HP Book #" + str(i)] = len(tokenized)
    print (length_dict)
    print ("There are %d words in the seven Harry Potter books!" % sum(length_dict.values()))

count_words()
