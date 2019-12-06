#Prepare

def normalize(string):
    return unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')



def remove_special_characters(string):
    return re.sub(r"[^a-z0-9'\s]", '', string)


def remove_stopwords(string):
    words = string.split()
    filtered_words = [w for w in words if w not in stopword_list]
    joined_words = ' '.join(filtered_words)
    return joined_words