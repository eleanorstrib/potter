from nltk import pos_tag, sent_tokenize, Text, word_tokenize
from nltk.stem import WordNetLemmatizer

from words import sexist_words as w

# determine who the dialog is spoken by (character name/gender)
# check if there is an adjective associated with their speech
# put the adjective into a dict, m/f, count instances of the adjective

l = WordNetLemmatizer()

def tokenize_text(textfile):
    """
    Splits the source text into sentences then tokenizes each word
    in each sentence.  The result is a list of lists (full_text), where the
    interior lists are the sentences.
    """
    full_text = []
    textfile = open(textfile).read()
    # list of sentence strings
    s_tokens = sent_tokenize(textfile)
    # tokenize words in each sentence string and add to the master list
    for sent in s_tokens:
        s = word_tokenize(sent)
        full_text.append(s)
    return full_text

def classify_words(sentence):
    """
    Applies NLTK's word classifier to identify parts of speech and returns a list
    of sentences, each a list of tuples where the tuples are classified words.
    """
    tagged_text = pos_tag(sentence)
    return tagged_text

def find_character(full_text, char):
    char_s = []
    for s in full_text:
        if char in s:
            char_s.append(s)
    return char_s

def char_plus_three(char, classified):
    plus_two = []
    for s in classified:
        if (char, 'NNP') in s:
            char_index = s.index((char, 'NNP'))
            if s[char_index -1] != ('Aunt', 'NNP'):
                plus_two.append([s[char_index -2 : char_index + 3]])
                print(len(plus_two))
    return plus_two

def char_prox(char, classified):
    for s in classified:
        for item in s:
            if item[1] == 'JJ':
                print(item)

def s_word_detector(w, classified_list):
    """
    Returns a list of sentences that contain the sexist words.
    """
    s_words = list(w.keys())
    s_word_sentences = []
    for s in classified_list:
        word_in_s = any(w in s for w in s_words)
        if word_in_s == True:
            s_word_sentences.append(s)

    s_word_tagged = [classify_words(sent) for sent in s_word_sentences]
    adj_list = find_adjectives(s_word_tagged)
    print(adj_list)
    return adj_list



full_text = tokenize_text('corpus/hp1.txt')
character_sentences = find_character(full_text, 'Petunia')
classified = [classify_words(s) for s in character_sentences]
c2 = char_plus_three('Petunia', classified)
print(c2)
# s_sexist_words = s_word_detector(w, full_text)
