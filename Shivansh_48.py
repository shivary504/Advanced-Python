import re

sentence = input("Sentence: ")
 #r treats backslashes as a word too
 #\b marks the start and \b the end
 #\w means it counts letters and digits and + means it can have more than one 
words = re.findall(r'\b\w+\b', sentence)

print("Repeated Words:")

for word in set(words):
    count = words.count(word)
    if count > 1:
        print(f"{word}: {count} times")

