import re
def count_positives_sum_negatives(arr):
    pos_sum = 0
    neg_sum = 0
    for n in arr:
        if n > 0:
            pos_sum += 1
        elif n < 0:
            neg_sum += n
    if [pos_sum, neg_sum] == []:
        return [0, 0]
    elif arr == []:
        return []
    else:
        return [pos_sum, neg_sum]