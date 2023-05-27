def Maximum_SubArray_prodeuct(ls):
    if len(ls)==0:
        return 0
    res = ls[0]
    for i in range(len(ls)):
        value=1
        for j in range(i,len(ls)):
            value*=ls[j]
            res = max(res,value)
    return res






ls = [2,3,-2,4]
print(Maximum_SubArray_prodeuct(ls))