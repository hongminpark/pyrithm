<h3>solution1</h3>

```python

def solution(answers):
    p1 = [1,2,3,4,5]*2000
    p2 = [2,1,2,3,2,4,2,5]*1250 
    p3 = [3,3,1,1,2,2,4,4,5,5]*1000
    answer = []
    p1_ct, p2_ct, p3_ct = 0,0,0
    p_ct_li = [] 
    
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            p1_ct += 1
        if answers[i] == p2[i]:
            p2_ct += 1
        if answers[i] == p3[i]:
            p3_ct += 1
    p_ct_li.extend([p1_ct, p2_ct, p3_ct])
    print(p_ct_li)
    
    win = max(p_ct_li)
    for i, a in enumerate(p_ct_li):
        if win == a:
            answer.append(i+1)

    return(sorted(answer))
```
> 
