'''
Created on 27-Feb-2019

@author: Arpan Kundu
'''

import random

import numpy as np
import pandas as pd


def generateRandomIndex(max_elem):  # Returns a random number in the range [0, max_elem]
    return np.int(np.round(np.random.random() * max_elem))


def generateRandomNumber(max_elem):  # Returns a random number in the range [1, max_elem]
    return generateRandomIndex(max_elem - 1) + 1


if __name__ == "__main__":
    _phrase_1 = np.array(["open for all", "limited period job offer", "received your profile", "work less and get paid more", "simplest path to become a millionaire", "get hired today"])
    _phrase_2 = np.array(["travel reimbursement", "you are shortlisted", "call us", "meet us"])
    _nonSuspiciousPhrases = np.array(["role of a software developer", "role of a human resources director"])
    data = []
    for i in range(0, 7501):
        msg = []
        noOfSuspiciousPhrases = generateRandomNumber(6)
        for j in range(0, noOfSuspiciousPhrases):
            phrase_1_index = generateRandomIndex(5)
            phrase_1 = _phrase_1[phrase_1_index]
            phrase_2_index = generateRandomIndex(3)
            phrase_2 = _phrase_2[phrase_2_index]
            msg.append(phrase_1)
            msg.append(phrase_2)
        if generateRandomIndex(1) == 1:
            noOfNonSuspiciousPhrases = generateRandomNumber(2)
            for j in range(0, noOfNonSuspiciousPhrases):
                nonSuspiciousPhrase_index = generateRandomIndex(1)
                nonSuspiciousPhrase = _nonSuspiciousPhrases[nonSuspiciousPhrase_index]
                msg.append(nonSuspiciousPhrase)
        msg = random.sample(msg, len(msg))
        str = "["
        for m in msg:
            str = str + m + ":"
        str = str[:-1] + "]"
        data.append([i + 1, str])
    df = pd.DataFrame(data, columns=["Message ID", "Message Phrases"])
    df.to_csv("Sample_Data.csv")
    print("Sample data generated and saved in Sample_Data.csv")
