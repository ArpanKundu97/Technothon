'''
Created on 27-Feb-2019

@author: Arpan Kundu
'''

import pickle


def predictTrafficIn(id, filename, rules, reducedItemSet):  # Predict whether the communication is an attempt of human trafficking
    f = open(filename, "rb")
    file_content = str(f.read())
    f.close()
    
    print("SUSPICIOUS ITEMS PRESENT IN COMMUNICATION", id)
    count = 0
    suspiciousTypes = []
    for reducedItem in reducedItemSet:
        for item in reducedItemSet[reducedItem]:
            if item in file_content:
                count = count + 1
                suspiciousTypes.append(reducedItem)
                print(str(count) + ". " + item)
    
    print("\nSUSPICIOUS ITEM TYPES PRESENT IN COMMUNICATION", id)
    count = 0
    for suspiciousType in suspiciousTypes:
        count = count + 1
        print(str(count) + ". " + suspiciousType)
    
    print("\nSUSPICIOUS RULES SATISFIED BY COMMUNICATION", id)
    count = 0
    satCount = 0
    for rule in rules:
        count = count + 1
        rule = rule.split("->", -1)
        antecedent = rule[0].lstrip()[12:-4]
        consequence = rule[1].lstrip()[12:-3]
        if suspiciousTypes.__contains__(antecedent) and suspiciousTypes.__contains__(consequence):
            satCount = satCount + 1
            isSatisfied = "SATISFIED"
        else:
            isSatisfied = "NOT SATISFIED"
        print(str(count) + ". " + antecedent + " -> " + consequence + "\t" + isSatisfied)
    print()
    
    satisfactionPercentage = satCount / count
    print(satCount, "(", str(satisfactionPercentage) , "%) rule(s) satisfied.")
    
    if satCount > 10:  # If the number of rules satisfied is greater than a predefined threshold, the communication is predicted to be an attempt of human trafficking
        print("WARNING!!! The communication is a possible attempt of human trafficking")
    else:
        print("The communication is genuine.")
    print()


if __name__ == "__main__":
    f = open("reduction2type", "rb")
    reducedItemSet = pickle.load(f)
    f.close()
    f = open("assocRules", "rb")
    rules = pickle.load(f)
    f.close()
    
    predictTrafficIn(1, "communication_1.txt", rules, reducedItemSet)
    predictTrafficIn(2, "communication_2.txt", rules, reducedItemSet)
