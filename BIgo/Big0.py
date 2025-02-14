def pair_sum_Sequence(n):
    tot=0
    for i in range(n):
        tot=tot+pair_sum(i,i+1)
    return tot
def pair_sum(a,b):
    return a+b
print(pair_sum_Sequence(4))
