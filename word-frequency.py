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
    #print frequencyDictionary
	#print frequencyDictionary["One"]
    return frequencyDictionary

wordFrequency("One Two Three Three Three Four Four Four Four Five Six")