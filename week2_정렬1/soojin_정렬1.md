<h3>solution1</h3>

```python
def solution(array, commands):
    answer = []

    for cmd in commands: 
        ans = sorted(array[cmd[0]-1:cmd[1]])[cmd[2]-1]
        answer.append(ans)
    
    return answer
```
> 
