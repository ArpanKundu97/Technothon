'''
Created on 27-Feb-2019

@author: Arpan Kundu
'''

from itertools import combinations
import pickle


def aprioriGen (L,  # Set of large frequent (i - 1)-item sets
                i
                ):
    C = []
    for I in L:  # For each large frequent (i - 1)-item set, I
        for J in L:
            if I == J:
                continue  # For each large frequent (i - 1)-item set, J != I
            if len(I.intersection(J)) == (i - 2):  # If I and J have (i - 2) common elements
                C.append(I.union(J))  # Insert I U J into Ci
    C = set (C)
    
    # PRUNING STEP
    pruned_C = []
    for c in C:  # For each candidate i-item set, c
        f = 1
        for subset in combinations (c, i - 1):  # For each subset of size (i - 1) of c,
            subset = frozenset(subset)
            if not (subset in L):  # If subset does not belong to L (i - 1)
                f = 0  # Exclude c from Ci
                break
        if f == 1:
            pruned_C.append (c)
    return pruned_C

    
def apriori (D,  # Dataset
             I,  # Item Set
             min_support  # Minimum Support
             ):
    sizeOfDataset = len (D)
    D = set (frozenset (i) for i in D)
    L = {}
    k = 0
    C = {}
    C[1] = set (frozenset ([i]) for i in I)  # C1 = I
    count = {}
    while len(C[k + 1]) != 0:
        k = k + 1
        L[k] = []
        for T in D:  # For each transaction, T
            for i in C[k]:  # For each candidate item set, i
                if i < T:  # If i is a subset of T,
                    try:
                        count[i] = count[i] + 1  # Increment count
                    except:
                        count[i] = 1
        for i in C[k]:  # For each candidate item set, i
            try:
                if count[i] >= min_support * sizeOfDataset:  # If minimum support is met,
                    L[k].append(i)  # Insert i into Lk
            except:
                continue
        L[k] = set (L[k])
        C[k + 1] = aprioriGen(L[k], k + 1)  # Generate the set of candidate (k + 1)-item sets
    return (L, count)

    
def assocGen (D,  # Dataset
              I,  # Item Set
              min_support,  # Minimum Support
              min_confidence  # Minimum Confidence
              ):
    (L, count) = apriori (D, I, min_support)  # L = Set of Large Frequent Item Sets
    
    print ("LARGE FREQUENT ITEM SETS")
    for l in L:
        if len (L[l]) > 0:
            print ("L" + str(l) + ": " + str(L[l]))
    print ()
    
    noOfAssoc = 0
    print ("ASSOCIATION RULES")
    rules = []
    for i in L:
        
        # No association rules can be generated from L1,
        # where L1 = Set of large frequent 1-item sets
        if i == 1:
            continue
        
        # If size of Li becomes equal to 0, processing can be stopped
        if len (L[i]) == 0:
            break
        
        for l in L[i]:  # For each large frequent item set, l
            for j in range (1, i):
                for subset in combinations (l, j):  # For each subset of l, do
                    subset = frozenset(subset)
                    if count[l] / count[subset] >= min_confidence:
                        print (str(subset) + " -> " + str(l.difference(subset))  # subset -> l - subset
                               +", Support = " + str (count[l] / len (D))
                               +", Confidence = " + str (count[l] / count[subset]))
                        noOfAssoc = noOfAssoc + 1
                        rules.append(str(subset) + " -> " + str(l.difference(subset)))
    print ()
    print ("Total Number of Rules:", noOfAssoc)
    
    # Save association rules
    f = open("assocRules", "wb")
    pickle.dump(rules, f)
    f.close()
