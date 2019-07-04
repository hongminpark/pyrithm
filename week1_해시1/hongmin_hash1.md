<h3>solution1. 정확성O/효율성X</h3>

```python
def solution(participant, completion):
    for i in completion:
        participant.remove(i)

    return participant[0]
```
    
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
