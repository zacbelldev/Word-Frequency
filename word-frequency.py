import re

def wordFrequency(sentence):
    frequencyDictionary = {}

    sentence = re.sub(r'[^\w\s]', ' ', sentence)
    # [ ^ ...] Matches any single character not in brackets
    # \w Matches word characters.
    # \s Matches whitespace.

    words = sentence.lower().split()
    # take the sentence string, make all characters lowercase, and then split into words

    for word in words:
        if word in frequencyDictionary:
            frequencyDictionary[word] += 1
        else:
            frequencyDictionary.update({word:1})
    print "Word Frequency...."
    for entry in frequencyDictionary:
        print "The word", entry, "occurred", frequencyDictionary[entry], "times."
    return frequencyDictionary
    # end word frequency function

wordFrequency("Exclamation! exclamation hyphen-hyphen Three Three--Four Four 'Four' four; Five SIX")


"""
---Output---

Word Frequency....
The word exclamation occurred 2 times.
The word four occurred 4 times.
The word five occurred 1 times.
The word hyphen occurred 2 times.
The word six occurred 1 times.
The word three occurred 2 times.
"""
