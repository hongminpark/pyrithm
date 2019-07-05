"""
동명이인 없을 경우, set 함수를 통해 count 할 필요 없이 바로 return해서 효율성 향상.
*set: 중복 제거
"""


#!/usr/bin/env python
# coding: utf-8

# In[18]:


import collections

def solution(participant, completion):
    
    diff = set(participant) - set(completion);
    if len(diff) > 0:
        return list(diff)[0];
    
    a = collections.Counter(participant);
    b = collections.Counter(completion);
    
    
    for k in a.keys():
        if b.get(k) != a.get(k):
            return k;


# In[ ]:





# In[ ]:




