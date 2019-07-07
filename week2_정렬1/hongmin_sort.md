<h3>solution1</h3>

```python
def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        array_ = array[i-1:j]
        array_.sort()
        answer.append(array_[k-1])
    
    return answer
```
> 


<h3>solution1'</h3>

```python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command        
        answer.append(sorted(array[i-1:j])[k-1])
    return answer
```
> 

