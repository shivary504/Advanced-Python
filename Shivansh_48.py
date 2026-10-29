#Question 1
import re

sentence = input("Sentence: ")
words = re.findall(r'\b\w+\b', sentence)

print("Repeated Words:")

for word in set(words):
    count = words.count(word)
    if count > 1:
        print(f"{word}: {count} times")

#Question 2 
import numpy as np

econs = np.array([10, 12, 15, 11, 14, 16, 13, 18, 12, 19])

print("Electricity econs:", econs)

print("First 4 Days:", econs[:4])
print("Days 6 to 9:", econs[5:9])

print("Total econs:", np.sum(econs))
print("Average econs:", np.mean(econs))
print("Maximum econs:", np.max(econs))
print("Minimum econs:", np.min(econs))

new_econs = econs + 2

print("Modified econs:", new_econs)
