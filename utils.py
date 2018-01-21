import csv
import string
from nltk import pos_tag, Text, word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

sp = string.punctuation + '``' + '...' + "--" + "''" + '‘' + '’'
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


def find_dialog(full_dict):
    for s in full_dict['HP1']:
        if s[0] == "''":
            print(s)
    # HP1 = pos_tag(full_dict['HP1'])
    # for i in range(len(HP1)):
    #     if HP1[i][0] == "''" or HP1[i][0] == '``':
    #         while


def read_text(num):
    with open('corpus/hp' + str(num) + '.txt', 'r') as f:
        book = f.read()
    f.close()
    return book

def text_tokenize(book):
    tokenize = word_tokenize(book)
    return tokenize

def tagging(tokenize):
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

def summarize_text(proper_nouns):
    counts = Counter(proper_nouns)
    return counts

def create_csv(nouns_count):
    nc = dict(nouns_count)
    for i in range(1, 8):
        with open('hp' + str(i) + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
            for k, v in nc.items():
                writer.writerow([k, v])

for i in range(1,8):
    a = read_text(i)
    b = text_tokenize(a)
    c = tagging(b)
    d = summarize_text(c)
    e = create_csv(d)
# tokenized = tokenize_punct()
# dialog_found = find_dialog(tokenized)
# name_nouns = name_nouns(tokenized, num_most_common, titles)
# word_count = count_words(tokenized)
