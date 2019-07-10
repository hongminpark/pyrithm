def solution(answers):
    s1 = [1, 2, 3, 4, 5]                #수포자1: 5개씩 반복
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]       #수포자2: 8개씩
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #수포자3: 10개씩
    s = [s1, s2, s3]
    cnt = [0, 0, 0]
    answer = []
            
    for i in range(3):
        for j in range(len(answers)):
            if s[i][j % len(s[i])] == answers[j]:
                cnt[i] += 1
            #for문 내에서 인덱스 초기화 불가능한지?
                     
    m = max(cnt)
    if m != 0:
        for i in range(3):
            if cnt[i] == m:
                answer.append(i + 1)
    return answer
