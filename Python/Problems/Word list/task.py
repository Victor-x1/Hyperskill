text = [
    ["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
    ["Ephemeral", "lasts", "one", "day", "only"],
    ["Accolade", "is", "an", "expression", "of", "praise"]]

# Nested List Comprehension Version
n = int(input())
print([text for sublist in text for text in sublist if len(text) <= n])

# Nested For Loop Version
"""n = int(input())
words = []
for sublist in words:
    for words in sublist:
        if len(words) < n:
            words.append(text)
print(words)
"""
