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




