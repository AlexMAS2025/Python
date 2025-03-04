def commun1(word1 = 'anticonstitutionnellement', word2 = 'ecclésiastique'):
    common = set(word1) & set(word2)
    return common

print(set(sorted(commun1())))

def commun2(word1 = 'anticonstitutionnellement', word2 = 'ecclésiastique'):
    common = list(w for w in word1 if w in word2)
    return common


print(set(sorted(commun2())))