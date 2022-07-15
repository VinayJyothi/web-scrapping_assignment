#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
import requests


# In[2]:


url = "https://quotes.toscrape.com/"


# In[3]:


response = requests.get(url)


# In[4]:


response.status_code


# In[7]:


soup = bs(response. content, 'html.parser')


# In[8]:


quote = soup.find('span' ,class_ = 'text')


# In[10]:


quote.text


# In[17]:


quotes = soup.find_all('span' ,class_ = 'text')


# In[18]:


quotes


# In[19]:


quotes = [quote.text[1:-1] for quote in quotes]


# In[21]:


quotes


# In[22]:


authors = soup.find_all('small' ,class_ ="author" )


# In[23]:


authors


# In[24]:


authors = [author.text for author in authors]


# In[25]:


authors


# In[26]:


tags = soup.find_all('div' , class_ = "tags")


# In[27]:


tags


# In[28]:


tags[0]


# In[30]:


tags[0].find_all('a' , class_ = "tag")


# In[32]:


for i in tags[0]. find_all('a' , class_ = "tag"):
    print(i.text)


# In[43]:


total_tags = []
for i in range(len(tags)):
    k=[]
    for j in tags[i].find_all('a' , class_ ="tag"):
        k.append(j.text)
    total_tags.append(','.join(k))


# In[44]:


total_tags


# In[45]:


import pandas as pd


# In[46]:


dataset = pd.DataFrame()


# In[47]:


dataset['Quotes'] = quotes


# In[48]:


dataset


# In[49]:


dataset['Quotes'] = quotes
dataset['Quote Tags'] = total_tags
dataset['Author'] = authors
dataset


# In[51]:


dataset.to_csv('quotes.csv')


# In[ ]:




