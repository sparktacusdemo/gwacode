import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import word_tokenize
import string

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

z = RegexpTokenizer(r"'[^']*'|[\w\']+").tokenize(text2)
z1 = [word.lower() for word in z]

stri = "'reflexion mirror'"

sen = "I am attaching my c.v. to this e-mail."
w = sen.count("attaching my c.v. to this e-mail")

#y = [wnl.lemmatize(word) for word in nltk.wordpunct_tokenize(sentence)]
# ['All', 'the', 'team', 'have', 'been', 'working', 'together']
print(z)
print(z1)
print(str(z1.count(stri.lower())) + " occurrence(s) for word: '" + stri + "'")
