import math
from collections import Counter

query = "nearest hairdresser maastricht"

documents = {
    "Doc1": "Hairdresser Maastricht city center walk in appointments",
    "Doc2": "Pizza restaurant Maastricht near station",
    "Doc3": "Hair salon near Maastricht station for women and men",
    "Doc4": "Beauty salon and hairdresser in Maastricht with online booking",
    "Doc5": "Bike repair shop Maastricht"
}

def tokenize(text):
    return text.lower().split()

query_tokens = tokenize(query)

print("\n1 QUERY TOKENS")
print(query_tokens)

print("\n2 DOCUMENT TOKENS")
doc_tokens = {}

for docid, text in documents.items():
    tokens = tokenize(text)
    doc_tokens[docid] = tokens
    print(docid, tokens)

N = len(documents)

print("\n3 NUMBER OF DOCUMENTS")
print(N)

def document_frequency(term):
    count = 0

    for tokens in doc_tokens.values():
        if term in tokens:
            count += 1

    return count

print("\n4 DOCUMENT FREQUENCY")
for term in query_tokens:
    print(term, document_frequency(term))

def idf(term):
    df = document_frequency(term)
    return math.log((N + 1) / (df + 1)) + 1

print("\n5 IDF VALUES")
for term in query_tokens:
    print(term, round(idf(term), 3))

def score_document(query_tokens, document_tokens):
    counts = Counter(document_tokens)
    score = 0

    for term in query_tokens:
        tf = counts[term]
        score += tf * idf(term)

    return score

print("\n6 DOCUMENT SCORES")
scores = {}

for docid, tokens in doc_tokens.items():
    score = score_document(query_tokens, tokens)
    scores[docid] = score
    print(docid, round(score, 3))

ranked_docs = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\n7 FINAL RANKING")
for docid, score in ranked_docs:
    print(docid, round(score, 3), documents[docid])

print("\n8 LEXICAL GAP EXAMPLE")
print("Doc3 says hair salon, not hairdresser.")
print("A keyword model gives Doc3 lower score even though salon is related to hairdresser.")

print("\n9 CROSS ENCODER IDEA")
print("BM25 gives candidates fast.")
print("CrossEncoder reads query and document together.")
print("It can understand that hairdresser and salon are semantically related.")
print("Then it reranks the top documents.")