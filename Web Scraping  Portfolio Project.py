#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')


# In[2]:


from bs4 import BeautifulSoup as bs


# In[3]:


import requests
from csv import writer


# In[4]:


url='https://www.amazon.in/s?k=watches'


# In[5]:


page=requests.get(url)
page


# In[6]:


soup=bs(page.content,'html.parser')
print(soup.prettify())


# In[7]:


soup.text


# In[8]:


image=soup.findAll('div',class_='s-image-padding')


# In[9]:


image


# In[10]:


img=[]


# In[11]:


for i in image:
    j=i.img['src']
    print(j)
   


# In[12]:


links=[]


# In[13]:


link=soup.findAll('span',class_='a-size-base-plus a-color-base a-text-normal')


# In[14]:


link


# In[15]:


brand=soup.findAll('span',class_='a-size-base-plus a-color-base')


# In[16]:


stars=soup.findAll('div',class_='a-section a-spacing-none a-spacing-top-micro')
stars


# In[17]:


price=soup.findAll('span',class_='a-price-whole')
stars


# In[18]:


delivery=soup.findAll('span',class_='a-color-base')
delivery


# In[19]:


offer=soup.findAll('div',class_='a-row a-size-small')


# In[20]:


offer


# In[21]:


number_of_ratings=soup.findAll('div',class_='a-row a-size-small')


# In[22]:


number_of_ratings


# In[ ]:




