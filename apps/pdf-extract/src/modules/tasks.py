import nltk

def text_extraction(element):
    # Extracting the text from the in-line text element
    line_text = element.get_text()
    
    # Return the text in each line
    return line_text

def count_occurrences_in_text(word,text):
    #convert text and word to lower case to make the count non sensitive to case
    wnl = nltk.WordNetLemmatizer()
    text_nltk = nltk.wordpunct_tokenize(text)
    word_lower_case = word.lower()
    return text_nltk.count(word_lower_case)
