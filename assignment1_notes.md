# Assignment 1 Tokenization

## Big picture

Tokenization is the first step in IRTM.

Raw text cannot directly be used by a search engine or NLP model.

The flow is

raw text  
to sentence tokens  
to word tokens  
to cleaned regex tokens  
to vocabulary  
to stopword removal  
to stemming or lemmatization  
to WordPiece tokenization  

## Running example

Raw query

Nearest Hairdresser? In @MaasTRICHcht!!

After lowercase and regex

nearest hairdresser in maastricht

After stopword removal

nearest hairdresser maastricht

## Sentence tokenization

sent_tokenize splits long text into sentences.

## Word tokenization

word_tokenize splits text into words and punctuation.

It keeps more information than simple split.

## Regex tokenization

RegexpTokenizer with r"\w+" keeps letters, numbers and underscores.

It removes punctuation like question marks and exclamation marks.

Problem is that it can break emails and special forms.

john.doe@example.com becomes john doe example com.

## Vocabulary

Vocabulary means every unique token once.

Code pattern:

vocab = sorted(set(tokens))

'set' removes duplicates.

'sorted'  puts tokens in order.

## Stopwords

Stopwords are common words like in, the, is, and.

Removing them can help old search systems.

But it can hurt meaning.

Example

'not good'

If not is removed, the meaning changes.

## Stemming

Stemming cuts suffixes using rules.

It is fast but rough.

Example

hairdresser becomes hairdress

## Lemmatization

Lemmatization maps words to real dictionary base forms.

It is cleaner than stemming.

With POS information it works better.

Example

is becomes be  
better becomes good  
playing becomes play  

## WordPiece

WordPiece breaks rare words into subword pieces.

It is used in BERT style models.

Example

unfathomable can be split into smaller pieces instead of becoming unknown.

## Exam answer

Tokenization converts raw text into meaningful units for search and NLP. Different tokenizers handle punctuation, case, contractions, rare words and domain terms differently. Bad tokenization can damage retrieval quality.