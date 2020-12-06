import random
wordList = open('words.list').read().split()
print(f"Random Word: {random.choice(wordList)}")