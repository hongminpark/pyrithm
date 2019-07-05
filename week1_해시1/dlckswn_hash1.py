def solution(participant, completion):
    if len(participant) > 100000 or len(participant) < 1:
        print("!!!마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.")
        return
    elif len(completion) != len(participant) - 1:
        print("!!!completion의 길이는 participant의 길이보다 1 작습니다.")
        return
    else:
        #테스트는 통과함
        cnt = 0
        for i in range(len(completion)):
            for j in range(len(participant)):
                if completion[i] == participant[j]:
                    cnt += 1
                    participant[j] = "0"
                    if cnt == len(completion):
                        for k in range(len(participant)):
                            if participant[k] != "0":
                                return participant[k]
        """
        for i in range(len(completion)):
            if participant[0] == completion[i]:
                if len(completion) > 1:
                    del participant[0]
                    i = 0
                else:
                    return participant[0]
        for i in range(len(participant)):
            if len(completion) > 0:
                x = 0
                if participant[i] != "999" and participant[i] == completion[x]:
                    del completion[0]
                    participant[i] = "999"
                else:
                    x += 1
            else:
                for j in range(len(participant)):
                    if participant[j] != "999":
                        return participant[j]
        """
