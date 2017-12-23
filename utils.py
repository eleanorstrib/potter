import string
from nltk import Text, word_tokenize

sp = string.punctuation + '``' + '...' + "--" + "''"

def quick_tokenize():
    full_dict= {}
    for i in range(1, 8):
        textfile = open('corpus/hp' + str(i) + '.txt').read()
        tokenized = word_tokenize(textfile)
        tokenized = [t for t in tokenized if t not in sp and t != "'s"]
        full_dict['HP' + str(i)] = tokenized
    print("Tokenized all 7 books.")
    return full_dict

def count_words(tokenized):
    length_dict = {}
    for i in range(1, 8):
        length_dict["HP Book #" + str(i)] = len(tokenized['HP' + str(i)])
        print ("HP%d is %d words long!" % (i, length_dict["HP Book #" + str(i)]))
    print ("There are %d words in the seven Harry Potter books!" % sum(length_dict.values()))
    print (length_dict)

tokenized = quick_tokenize()
word_count = count_words(tokenized)
