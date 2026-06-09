# Assignment 3 Search Engines

## Big picture

Assignment 3 starts after document representation.

Assignment 1 cleaned text.

Assignment 2 turned text into vectors.

Assignment 3 builds a search engine that retrieves and ranks documents for a query.

The flow is

query  
to tokens  
to candidate documents  
to BM25 ranking  
to cross encoder reranking  
to evaluation  

## Running example

Query

nearest hairdresser maastricht

Documents

Doc1 Hairdresser Maastricht city center  
Doc2 Pizza restaurant Maastricht  
Doc3 Hair salon near Maastricht station  
Doc4 Beauty salon and hairdresser Maastricht  
Doc5 Bike repair shop Maastricht  

## Search index idea

A search engine does not scan every document slowly.

It builds an inverted index.

Example

hairdresser maps to Doc1 and Doc4  
maastricht maps to Doc1, Doc2, Doc3, Doc4 and Doc5  
salon maps to Doc3 and Doc4  

This lets the engine retrieve candidates quickly.

## BM25 idea

BM25 is a lexical ranking model.

It ranks documents based on exact word overlap between query and document.

It uses

term frequency  
inverse document frequency  
term frequency saturation  
document length normalization  

## IDF idea

Rare words are more useful.

maastricht appears in many documents, so it is less informative.

hairdresser appears in fewer documents, so it has more weight.

## Lexical gap

BM25 can fail when the query and document use different words with the same meaning.

Example

Query uses hairdresser.

Document uses hair salon.

BM25 may not understand that they are related because it mainly depends on exact word matching.

## Cross encoder

A cross encoder reads the query and document together.

It can understand semantic relevance better than BM25.

Example

nearest hairdresser maastricht

and

hair salon near Maastricht station

are semantically related.

The cross encoder can give this pair a high relevance score.

## Reranking

BM25 is used first because it is fast.

Cross encoder is used second because it is smarter but slower.

The pipeline is

BM25 retrieves top candidate documents  
Cross encoder scores query document pairs  
documents are sorted again by cross encoder score  

## Exam answer

A search engine first retrieves candidate documents using a fast lexical method like BM25. BM25 uses term frequency, inverse document frequency and length normalization. Since BM25 can miss semantic matches due to the lexical gap, neural reranking with a cross encoder can improve the ranking by reading the query and passage together.