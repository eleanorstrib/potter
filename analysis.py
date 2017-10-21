from nltk import pos_tag, sent_tokenize, word_tokenize

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

    print(full_text.similar('Hermoine'))
    return full_text

def classify_words(tokens):
    """
    """
    for sent in full_text:
        # list of tuples that look like this ('summer', 'NN'), ("''", "''")
        tagged_text = pos_tag(sent)

        print(tagged_text)

full_text = tokenize_text('corpus/hp1.txt')
print(full_text)
classify_words(full_text)
