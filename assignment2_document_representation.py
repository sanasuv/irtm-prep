from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#from sentence_transformers import SentenceTransformer

query = "nearest hairdresser maastricht" 
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

query = "nearest hairdresser maastricht"

documents = [
    "Hairdresser Maastricht city center walk-in appointments",
    "Pizza restaurant Maastricht near station",
    "Hair salon near Maastricht station for women and men",
    "Beauty salon and hairdresser in Maastricht with online booking"
]

all_texts = [query] + documents

print("\n1 RAW QUERY")
print(query)

print("\n2 DOCUMENTS")
for i, doc in enumerate(documents, start=1):
    print(f"Doc{i}:", doc)

count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(all_texts)

print("\n3 COUNT VECTORIZER VOCABULARY")
print(count_vectorizer.get_feature_names_out())

print("\n4 COUNT MATRIX")
print(count_matrix.toarray())

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)

print("\n5 TF-IDF VOCABULARY")
print(tfidf_vectorizer.get_feature_names_out())

print("\n6 TF-IDF MATRIX")
print(tfidf_matrix.toarray().round(3))

query_vector = tfidf_matrix[0]
document_vectors = tfidf_matrix[1:]

tfidf_similarities = cosine_similarity(query_vector, document_vectors)

print("\n7 TF-IDF COSINE SIMILARITY")
for i, score in enumerate(tfidf_similarities[0], start=1):
    print(f"Query vs Doc{i}: {score:.3f}")

ranked_docs = sorted(
    enumerate(tfidf_similarities[0], start=1),
    key=lambda x: x[1],
    reverse=True
)

print("\n8 FINAL TF-IDF RANKING")
for doc_id, score in ranked_docs:
    print(f"Doc{doc_id}: {score:.3f}")
    print(documents[doc_id - 1])

documents = [
    "Hairdresser Maastricht city center walk-in appointments",
    "Pizza restaurant Maastricht near station",
    "Hair salon near Maastricht station for women and men",
    "Beauty salon and hairdresser in Maastricht with online booking"
]

all_texts = [query] + documents

print("\n1 RAW QUERY")
print(query)

print("\n2 DOCUMENTS")
for i, doc in enumerate(documents, start=1):
    print(f"Doc{i}:", doc)

# -----------------------------
# PHASE 1: COUNT VECTORS
# -----------------------------

count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(all_texts)

print("\n3 COUNT VECTORIZER VOCABULARY")
print(count_vectorizer.get_feature_names_out())

print("\n4 COUNT MATRIX")
print(count_matrix.toarray())

# -----------------------------
# PHASE 2: TF-IDF VECTORS
# -----------------------------

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)

print("\n5 TF-IDF VOCABULARY")
print(tfidf_vectorizer.get_feature_names_out())

print("\n6 TF-IDF MATRIX")
print(tfidf_matrix.toarray().round(3))

# -----------------------------
# PHASE 3: COSINE SIMILARITY
# -----------------------------

query_vector = tfidf_matrix[0]
document_vectors = tfidf_matrix[1:]

tfidf_similarities = cosine_similarity(query_vector, document_vectors)

print("\n7 TF-IDF COSINE SIMILARITY")
for i, score in enumerate(tfidf_similarities[0], start=1):
    print(f"Query vs Doc{i}: {score:.3f}")

# -----------------------------
# PHASE 4: SENTENCE TRANSFORMER
# -------------------------