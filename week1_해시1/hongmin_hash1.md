<h3>solution1. 정확성O/효율성X</h3>

```python
def solution(participant, completion):
    for i in completion:
        participant.remove(i)

    return participant[0]
```
> 효율성 0 why ?:  remove() 시간복잡도 n <br>
(For 루프) * (remove) = > n *n의 시간복잡도  <br>
- 리스트에서 아이템 바로 삭제: remove <br>
- 리스트에서 인덱스로 삭제: pop <br>
(REMOVE는 시간복잡도 N이고 POP은 1)<br>





<h3>solution2. 효율성O/정확성O</h3>

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for idx,item in enumerate(completion):
        if item is not participant[idx]:
            return participant[idx]
    return participant[-1]
```
> 리스트 두개를 sorting한다음(효율성 향상)에 for 루프로 한명씩 비교를 하는 것<br>
소팅된 part=[a,b,c,c,d]<br>
소팅된 com=[a,b,c,d] <br>
이렇게라면 for루프를 돌려서 리스트 하나하나 값을 비교해서 중간에 값이 다른애가있으면 <br>
고놈이 통과 못한 애인거쥐<br>
*Enumerate : 리스트에서 인덱스랑 값을 같이 뱉어줌 <br>
