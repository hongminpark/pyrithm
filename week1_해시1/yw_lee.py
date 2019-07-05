from collections import Counter

def solution(participant, completion):
    
    
    result = Counter(participant)
    result2 = Counter(completion)
    preanswer = (result - result2)
    
    answer = []
    for key in preanswer:
        answer.append(key)
    
    return answer[0]
