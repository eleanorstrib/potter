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


def find_character(w, classified_list, character):
    s_words = list(w.keys())
    count = 0
    for s in classified_list:
        word_in_s = any(w in s for w in s_words)
        if word_in_s == True:
            count+=1
    print(count)
    print(len(classified_list))
    #     for word in s_words:
    #         if word in s:
    #             found_word = word
    #             found_index = s.index(word)
    #             print(s)

        #     print(c)



full_text = tokenize_text('corpus/hp1.txt')
find_character(w, full_text, 'Hermione')
