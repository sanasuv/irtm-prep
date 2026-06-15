# Assignment 2 Document Representation

## Big picture

After tokenization, the machine still cannot understand text.

So Assignment 2 asks how to convert text into numbers.

The flow is

documents  
to vocabulary  
to count vectors  
to TF-IDF vectors  
to cosine similarity  
to embeddings  
to sentence transformers  

## Running example

Query

nearest hairdresser maastricht

Documents

Doc1 Hairdresser Maastricht city center  
Doc2 Pizza restaurant Maastricht  
Doc3 Hair salon near Maastricht station  
Doc4 Beauty salon and hairdresser Maastricht  

## CountVectorizer

CountVectorizer builds a vocabulary and counts how many times each word appears.

Code pattern

count_vectorizer = CountVectorizer()  
count_matrix = count_vectorizer.fit_transform(all_texts)

fit learns the vocabulary.

transform converts text into vectors.

Problem

It only counts exact words.

It does not understand that hairdresser and salon are related.

## TF-IDF

TF-IDF gives lower weight to common words and higher weight to rare useful words.

maastricht appears in many documents, so it is less useful.

hairdresser appears in fewer documents, so it becomes more important.

Code pattern

tfidf_vectorizer = TfidfVectorizer()  
tfidf_matrix = tfidf_vectorizer.fit_transform(all_texts)

## Cosine similarity

Cosine similarity compares the direction of vectors.

If query and document have similar word importance, the cosine score is high.

Code pattern

cosine_similarity(query_vector, document_vectors)

A high score means the document is close to the query.

## Word2Vec and GloVe idea

TF-IDF is count based.

Word2Vec and GloVe are meaning based.

They learn word vectors from context.

So hairdresser and salon can become close in vector space.

Weakness

Word2Vec and GloVe are static.

The same word gets the same vector in every context.

## Sentence Transformers

Sentence Transformers embed the whole sentence.

They understand context better than simple word averaging.

So

nearest hairdresser maastricht

can match

hair salon near Maastricht station

even if the exact word hairdresser is missing.

## Exam answer

Document representation converts text into numerical vectors. CountVectorizer counts word frequency, TF-IDF weights words by importance, cosine similarity compares document vectors, and embeddings represent semantic meaning beyond exact word overlap.
