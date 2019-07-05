"""
동명이인 없으면 else 타고, 동명이인 있으면 counter 로 1개 이상인 애 내뱉음 

But, 
part, comp = ['a','a','b','b','c','c','c'], ['a','a','b','b','c','c'] 
solution(part,comp) => ['a', 'b', 'c']

동명이인 여러 개일 경우 오류! 카운터끼리 빼는 과정이 필요할 듯 
"""


from collections import Counter

def solution(participant, completion):
    completion = set(completion)
    answer = [x for x in participant if x not in completion]
    if answer == []:
        return [k for k,v in Counter(participant).items() if v>1]
    else:
        return answer




participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))


