<h3>solution1</h3>

```python
def solution(answers):
    count = [0, 0, 0]
    result = []
    for idx, ans in enumerate(answers):
        if ans is ans_1(idx):
            count[0] += 1
        if ans is ans_2(idx):
            count[1] += 1
        if ans is ans_3(idx):
            count[2] += 1
    
    for i, idx in enumerate(count):
        if i is max(count):
            result.append(idx+1)
    
    return result
        
        
def ans_1(idx):
    if idx%5 is 0:
        return 5
    else:
        return idx%5

def ans_2(idx):
    if idx%2 is 1:
        return 2
    else:
        tmp = idx%8
        if tmp is 2:
            return 1
        elif tmp is 4:
            return 3
        elif tmp is 6:
            return 4
        else:
            return 5

def ans_3(idx):
    tmp = idx%10
    if tmp is 1 or 2:
        return 3
    elif tmp is 3 or 4:
        return 1
    elif tmp is 5 or 6:
        return 2
    elif tmp is 7 or 8:
        return 4
    else:
        return 5
```

> 




