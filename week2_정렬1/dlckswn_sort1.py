def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0] - 1:commands[i][1]] #여기서 바로 .sort()하면 값이 다르게 나옴 
        arr.sort()
        answer.append(arr[commands[i][2] - 1])
    return answer
