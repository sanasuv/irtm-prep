import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from transformers import AutoTokenizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

text = "Nearest Hairdresser? In @MaasTRICHcht!! Don't split john.doe@example.com. Playing football is unfathomable."

print("\n1 RAW TEXT")
print(text)

sentences = sent_tokenize(text)
print("\n2 SENTENCE TOKENIZATION")
print(sentences)

word_tokens = word_tokenize(text)
print("\n3 WORD TOKENIZATION")
print(word_tokens)

regex_tokenizer = RegexpTokenizer(r"\w+")
regex_tokens = regex_tokenizer.tokenize(text.lower())
print("\n4 REGEX TOKENIZATION")
print(regex_tokens)

vocab = sorted(set(regex_tokens))
print("\n5 VOCABULARY")
print(vocab)
print("Number of tokens:", len(regex_tokens))
print("Vocabulary size:", len(vocab))

stop_words = set(stopwords.words("english"))
tokens_without_stopwords = []

for token in regex_tokens:
    if token not in stop_words:
        tokens_without_stopwords.append(token)

print("\n6 AFTER STOPWORD REMOVAL")
print(tokens_without_stopwords)

stemmer = PorterStemmer()
stemmed_tokens = []

for token in tokens_without_stopwords:
    stemmed_tokens.append(stemmer.stem(token))

print("\n7 STEMMING")
print(stemmed_tokens)

lemmatizer = WordNetLemmatizer()
lemmatized_tokens = []

for token in tokens_without_stopwords:
    lemmatized_tokens.append(lemmatizer.lemmatize(token))

print("\n8 LEMMATIZATION WITHOUT POS")
print(lemmatized_tokens)

print("\n9 LEMMATIZATION WITH POS")
print("playing ->", lemmatizer.lemmatize("playing", pos="v"))
print("better ->", lemmatizer.lemmatize("better", pos="a"))
print("is ->", lemmatizer.lemmatize("is", pos="v"))

wordpiece_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
wordpiece_tokens = wordpiece_tokenizer.tokenize("Playing football is unfathomable.")

print("\n10 WORDPIECE TOKENIZATION")
print(wordpiece_tokens)

clean_query = " ".join(lemmatized_tokens)

print("\n11 FINAL CLEANED QUERY")
print(clean_query)