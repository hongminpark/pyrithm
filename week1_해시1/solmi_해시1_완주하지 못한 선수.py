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


