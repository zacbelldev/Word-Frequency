def wordFrequency(sentence):
    frequencyDictionary = {}
    words = sentence.split()
    for key in words:
        if key in frequencyDictionary:
            frequencyDictionary[key] += 1
        else:
            frequencyDictionary.update({key:1})
    print "Word Frequency...."
    for key in frequencyDictionary:
        print "the word", key, "occurred", frequencyDictionary[key], "times"
    return frequencyDictionary

wordFrequency("One Two Three Three Three Four Four Four Four Five Six")


"""
---Output---

Word Frequency....
the word Four occurred 4 times
the word Six occurred 1 times
the word Five occurred 1 times
the word One occurred 1 times
the word Three occurred 3 times
the word Two occurred 1 times

"""
