from nltk import pos_tag, sent_tokenize, Text, word_tokenize

# determine who the dialog is spoken by (character name/gender)
# check if there is an adjective associated with their speech
# put the adjective into a dict, m/f, count instances of the adjective


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

def classify_words(full_text):
    """
    Applies NLTK's word classifier to identify parts of speech and returns a list
    of sentences, each a list of tuples where the tuples are classified words.
    """
    classified_list = []
    for sent in full_text:
        # list of tuples that look like this ('summer', 'NN'), ("''", "''")
        tagged_text = pos_tag(sent)
        classified_list.append(tagged_text)
    return classified_list

def find_character(classified_list, character):
    for s in classified_list:
        if 'bossy' in s:
            print(s)


full_text = tokenize_text('corpus/hp1.txt')
find_character(full_text, 'Hermione')
