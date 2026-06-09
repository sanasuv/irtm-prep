# assignment4_evaluation.py

from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

print("\nQUERY")
print("nearest hairdresser maastricht")

# Ground truth
# What SHOULD be relevant

actual = [
    1,  # Doc1 relevant
    0,  # Doc2 not relevant
    1,  # Doc3 relevant
    1,  # Doc4 relevant
    0   # Doc5 not relevant
]

# Search engine prediction

predicted = [
    1,  # Doc1 returned
    1,  # Doc2 returned incorrectly
    1,  # Doc3 returned
    0,  # Doc4 missed
    0   # Doc5 ignored
]

print("\nACTUAL")
print(actual)

print("\nPREDICTED")
print(predicted)

cm = confusion_matrix(actual, predicted)

print("\nCONFUSION MATRIX")
print(cm)

precision = precision_score(actual, predicted)

recall = recall_score(actual, predicted)

f1 = f1_score(actual, predicted)

print("\nPRECISION")
print(round(precision,3))

print("\nRECALL")
print(round(recall,3))

print("\nF1")
print(round(f1,3))