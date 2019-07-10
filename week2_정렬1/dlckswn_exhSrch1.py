def solution(answers):
    s1 = [1, 2, 3, 4, 5]                #수포자1: 5개씩 반복
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]       #수포자2: 8개씩
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #수포자3: 10개씩
    s = [s1, s2, s3]
    cnt = [0, 0, 0]
    answer = []
            
    for i in range(3):
        if len(s[i]) >= len(answers):
            for j in range(len(answers)):
                if s[i][j] == answers[j]:
                    cnt[i] += 1
        else: #cnt 구한 뒤 몫만큼 곱하고 나머지만큼 더하기
            for j in range(len(s[i])):
                if s[i][j] == answers[j]:
                    cnt[i] += 1
            cnt[i] = cnt[i] * len(answers) // len(s[i]) #몫은 무조건 >= 1
            for k in range(len(answers) % len(s[i])): #테스트 케이스 55554
                if s[i][j] == answers[k]:
                    cnt[i] += 1
                     
    m = max(cnt)
    #if m != 0:
    for i in range(3):
        if cnt[i] == m:
            answer.append(i + 1)
    return answer
