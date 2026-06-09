# Assignment 4: Evaluation.

Goal: Measure whether the search engine is good.

Pipeline:
#--------------

Query
↓
BM25
↓
Cross Encoder
↓
Ranking
↓
Evaluation

Confusion Matrix

TP = relevant and returned

FP = returned but not relevant

FN = relevant but missed

TN = not relevant and not returned

Precision: TP / (TP + FP)
Measures correctness of returned documents.

Recall: TP / (TP + FN)
Measures completeness of retrieval.

F1: 2PR / (P + R)
Balances precision and recall.

Accuracy Problem: IR datasets are highly imbalanced.
A system can achieve high accuracy while retrieving useless results.

ROUGE: Measures overlap between generated and reference summaries.

PMI: Measures association between words.
High PMI means words frequently occur together.

Exam Answer:
Evaluation metrics measure search quality. Precision measures correctness, recall measures completeness, and F1 balances both. Confusion matrices provide TP, FP, FN and TN counts. ROUGE evaluates summaries and PMI measures word associations.