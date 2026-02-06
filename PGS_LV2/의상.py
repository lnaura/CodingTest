def solution(clothes):
    answer = 0
    category = {}
    for clothe_name, c in clothes:
        if c in category:
            category[c] += 1
        else:
            category[c] = 1
    
    answer = 1
    for value in category.values():
        answer *= value + 1 
    
    answer -= 1

    return answer

#----------------------------------
# Counter 사용
from collections import Counter
from math import prod

def solution(clothes):
    counts = Counter([kind for name, kind in clothes])
    
    return prod([c + 1 for c in counts.values()]) - 1