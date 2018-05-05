
import string
from nltk import pos_tag, Text, word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

from words import sexist_words as w

sp = string.punctuation + '``' + '...' + "--" + "''" + '‘' + '’'
lem = WordNetLemmatizer()
num_most_common = 250
titles = ['Lord', 'Mr.', 'Mrs.', 'Miss', 'Ms.', 'Professor', 'Minister',
        'Aunt', 'Uncle', 'Lady', 'Sir', 'Madame']

def quick_tokenize():
    full_dict= {}
    for i in range(1, 8):
        textfile = open('corpus/hp' + str(i) + '.txt').read()
        tokenized = word_tokenize(textfile)
        tokenized = [t for t in tokenized if t not in sp and t != "'s"]
        full_dict['HP' + str(i)] = tokenized
    print("Tokenized all 7 books.")
    return full_dict

def tokenize_punct():
    full_dict= {}
    for i in range(1, 8):
        textfile = open('corpus/hp' + str(i) + '.txt').read()
        s_tokens = sent_tokenize(textfile)
        tokenized = [t for t in s_tokens]
        text = []
        for sent in tokenized:
            s = word_tokenize(sent)
            text.append(pos_tag(s))
        full_dict['HP' + str(i)] = text
    print("Tokenized all 7 books by sentence with punctuation.")
    return full_dict

def count_words(tokenized):
    length_dict = {}
    for i in range(1, 8):
        length_dict["HP Book #" + str(i)] = len(tokenized['HP' + str(i)])
        print ("HP%d is %d words long!" % (i, length_dict["HP Book #" + str(i)]))
    print ("There are %d words in the seven Harry Potter books!" % sum(length_dict.values()))
    print (length_dict)

def name_nouns(full_dict, num_common, titles):
    list_names = []
    for book in full_dict.values():
        tagged_text = pos_tag(book)
        for w in range(len(tagged_text)):
            if tagged_text[w][1] == 'NNP':
                # attaches titles to names e.g. "Mrs. Weasley" and "Professor Dumbledore"
                if tagged_text[w][0] in titles:
                    list_names.append(tagged_text[w][0] + " " + tagged_text[w+1][0] + " ")
                    print(tagged_text[w+1])
                    w+=1
                else:
                    list_names.append(tagged_text[w][0])
    name_sum = Counter(list_names)
    print(name_sum.most_common(num_common))
    return name_sum

def tagging_nouns(tokenize):
    proper_nouns = []
    tag = pos_tag(tokenize)
    i = 0
    while i < len(tag):
        if tag[i][1] == 'NNP':
            if tag[i+1][1] == 'NNP':
                proper_nouns.append(tag[i][0].lower() + " " + tag[i+1][0].lower())
                i+=1 # extra increment added to the i counter to skip the next word
            else:
                proper_nouns.append(tag[i][0].lower())
        i+=1 # increment the i counter
    return proper_nouns

def find_sexist_words(text):
    for i in text:
        next = lem.lemmatize(i)
    if next in w:
