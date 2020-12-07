import random

def getword(channel):
    print(f"channel {channel}")
    if channel.startswith('xmas'):
        wordList = open('xmas.list').read().split()        
    else:        
        wordList = open('words.list').read().split()
    print(f"Random Word: {random.choice(wordList)}")

getword('xmfass')