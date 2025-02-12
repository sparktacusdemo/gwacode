import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import string
import re

sentence0 = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""

sentence1 = "hey! John O'maley is my friend!"
sentence = 'I am going to visit "Huge Hotel" and the "Grand River"'
sx = sentence.translate(dict.fromkeys(string.punctuation))

wnl = nltk.WordNetLemmatizer()
x = nltk.wordpunct_tokenize(sentence1)

y = [word.lower() for word in nltk.wordpunct_tokenize(sentence1)]

text = """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500


text2 = "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"
text3 = "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida"

#case2
#mytext = "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida" 
#case N
#mytext = "hey! John O'maley is my friend!"
#case1
#mytext = "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida"
#case3
#mytext = "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida"
#case4
#mytext = "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida"
#case N
#mytext = "who is approved by OILS is completely legitimate: their employees are of legal working age"

#case5
#mytext = "I hope you will consider this proposal, and get back to me as soon as possible"

#case 6
mytext = "When you know:get back to me"

# case 7&8
#mytext = "enable Delavigne and its subsidiaries to create a skin-care monopoly"


#mytext = "'''Linguist Specialist Found Dead on Laboratory Floor'''"
#mytext = "__Linguist Specialist Found Dead on Laboratory Floor__"

#stri = "'reflexion mirror'"
#stri = "maley"
#stri = "get back to me"
#stri = "reflexion mirror"
#stri = "skin-care monopoly"
stri = "get back to me"

#mytext2 = "Reflexion Mirror\" in Sopchoppy, Florida"
#mytext2 = "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida"

if re.search("(?<=\()[^]]+(?=\))", mytext):
    print("case1 \n")
    z = RegexpTokenizer(r"((?<=\()[^]]+(?=\))|\w+)").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("'[^']*'", mytext):
    print("case2 \n")
    z = RegexpTokenizer(r"'[^']*'|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("(?<=\u00ab)[^\u00ab|\u00bb]+(?=\u00bb)", mytext):
    print("case 3 \n")
    z = RegexpTokenizer(r"(?<=\u00ab)[^\u00ab|\u00bb]+(?=\u00bb)|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("(?<=\u201c)[^\u201c|\u201d]+(?=\u201d)", mytext):
    print("case 4 \n")
    z = RegexpTokenizer(r"(?<=\u201c)[^\u201c|\u201d]+(?=\u201d)|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("(?<=and\s)[^]]+(?=\s+as\s+soon)", mytext):
    print("case 5 \n")
    z = RegexpTokenizer(r"(?<=and\s)[^]]+(?=\s+as\s+soon)|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("(?<=\:)[^\:]+(?=$)", mytext):
    print("case 6 \n")
    z = RegexpTokenizer(r"(?<=\:)[^\:]+(?=$)|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("\w{0,1000}\-.*?(?=$)", mytext):
    print("case 7 \n")
    z = RegexpTokenizer(r"\w{0,1000}\-.*?(?=$)|\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("[\w\-]+", mytext):
    print("case 8 \n")
    z = RegexpTokenizer(r"[\w\-]+").tokenize(mytext)
    z1 = [word.lower() for word in z]
elif re.search("[\w\']+", mytext):
    print("case N \n")
    z = RegexpTokenizer(r"[\w\']+").tokenize(mytext)
    z1 = [word.lower() for word in z]
else:
    print("case else \n")
    z = RegexpTokenizer(r"\w+").tokenize(mytext)
    z1 = [word.lower() for word in z]

#z = RegexpTokenizer(r"(?<=\u00ab)[^]]+(?=\u00bb)|\w+").tokenize(mytext2)
#z1 = [word.lower() for word in z]


#y = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(sentence)]
# ['All', 'the', 'team', 'have', 'been', 'working', 'together']
print(z)
print(z1)
print(str(z1.count(stri.lower())) + " occurrence(s) for word: '" + stri + "'\n in sentence -> '" + mytext + "'")
