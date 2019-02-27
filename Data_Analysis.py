'''
Created on 27-Feb-2019

@author: Arpan Kundu
'''

import pickle

from AprioriImpl import assocGen
import pandas as pd

if __name__ == "__main__":
    traffic_data = "Sample_Data.csv"
    TrafficData = pd.read_csv (traffic_data)
    
    # Remove unnecessary columns
    TrafficData.pop("Unnamed: 0")
    TrafficData.pop("Message ID")
    
    # Data Reduction
    dataset = []  # Reduced set of messages
    reducedItemSet = {}  # Set of reduced phrases
    for index, row in TrafficData.iterrows():
        s = row["Message Phrases"]
        s = s [1 :-1]  # Removes '[' and ']'
        messagePhrases = s.split (':', -1)  # Returns an array of all the message phrases
        reducedMessagePhrases = []  # Array of all reduced phrases
        for messagePhrase in messagePhrases:
            messagePhrase = messagePhrase.lstrip()  # Removes leading white spaces
            
            # Reduce each message phrase to the portion which is suspicious
            if messagePhrase.startswith("open"):
                reducedMessagePhrase = "open" 
            elif messagePhrase.startswith("limited period"):
                reducedMessagePhrase = "limited period" 
            elif messagePhrase.startswith("work less"):
                reducedMessagePhrase = "work less" 
            elif messagePhrase.endswith("millionaire"):
                reducedMessagePhrase = "millionaire" 
            elif messagePhrase.endswith("shortlisted"):
                reducedMessagePhrase = "shortlisted" 
            elif messagePhrase.startswith("call"):
                reducedMessagePhrase = "call" 
            elif messagePhrase.startswith("meet"):
                reducedMessagePhrase = "meet" 
            elif messagePhrase.startswith("role"):
                reducedMessagePhrase = "role" 
            else:
                reducedMessagePhrase = messagePhrase
            reducedMessagePhrases.append(reducedMessagePhrase)  # Reduced message phrases are later checked for presence in a communication
            try:
                reducedItemSet[reducedMessagePhrase].add(messagePhrase)
            except:
                reducedItemSet[reducedMessagePhrase] = {messagePhrase}
        dataset.append (reducedMessagePhrases)
    
    # Print Hash Map
    index = 0
    count = 0
    print ("REDUCTION TO SUSPICIOUS SUB-PHRASE")
    for reducedItem in reducedItemSet:
        s = ""
        index = index + 1
        for item in reducedItemSet[reducedItem]:
            s = s + item + ", "
            count = count + 1
        print (str (index) + " " + reducedItem + ": " + s [0 :-2])
    print ("Total number of items:", count)
    print ()
    
    # Reduction of Phrase to Type
    finalDataset = []  # Final set of messages
    finalReducedItemSet = {}  # Set of message types
    for messagePhrases in dataset:
        reducedMessagePhrases = []  # Array of all message types
        for messagePhrase in messagePhrases:
            messagePhrase = messagePhrase.lstrip()  # Removes leading white spaces
            
            # Reduce each message phrase to its corresponding type
            if messagePhrase == "millionaire" or messagePhrase == "work less":
                reducedMessagePhrase = "high payment for minimal work" 
            elif messagePhrase == "received your profile" or messagePhrase == "shortlisted":
                reducedMessagePhrase = "suspicious recruitment" 
            elif messagePhrase == "get hired today" or messagePhrase == "limited period":
                reducedMessagePhrase = "quick recruitment" 
            elif messagePhrase == "call" or messagePhrase == "meet":
                reducedMessagePhrase = "communicate"
            else:
                reducedMessagePhrase = messagePhrase
            reducedMessagePhrases.append(reducedMessagePhrase)  # These phrases are fed into the apriori algorithm
            try:
                finalReducedItemSet[reducedMessagePhrase].add(messagePhrase)
            except:
                finalReducedItemSet[reducedMessagePhrase] = {messagePhrase}
        finalDataset.append (reducedMessagePhrases)
    
    # Print Hash Map
    index = 0
    count = 0
    print ("REDUCTION TO TYPE")
    for reducedItem in finalReducedItemSet:
        s = ""
        index = index + 1
        for item in finalReducedItemSet[reducedItem]:
            s = s + item + ", "
            count = count + 1
        print (str (index) + " " + reducedItem + ": " + s [0 :-2])
    print ("Total number of items:", count)
    print ()
    
    # Save reduction to type which will be later used for reducing phrases in a communication
    f = open("reduction2type", "wb")
    pickle.dump(finalReducedItemSet, f)
    f.close()

    # A-Priori Algorithm
    assocGen (finalDataset,  # Dataset
              finalReducedItemSet.keys(),  # Item Set
              0.002,  # Minimum Support
              0.5  # Minimum Confidence
              )
