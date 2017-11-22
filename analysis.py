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

def find_adjectives(tagged_list):
    for s in tagged_list:
        s_adj = [val for val in s if val[1]=='ADJ']
    print(s_adj)
    return s_adj

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
classified = [classify_words(s) for s in full_text]

# s_sexist_words = s_word_detector(w, full_text)
