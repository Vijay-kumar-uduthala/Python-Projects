#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
import requests


# In[10]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {'User-Agent': 'MyPythonScript/1.0 (https://example.com/contact)'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'html.parser')


# In[11]:


print(soup)


# In[40]:


soup.find('table')


# In[15]:


soup.find('table', class_ = 'wikitable sortable')


# In[ ]:





# In[41]:


table = soup.find_all('table')[0]


# In[43]:


world_titles = table.find_all('th')


# In[44]:


world_table_titles = [title.text.strip() for title in world_titles]
print(world_table_titles)


# In[45]:


import pandas as pd
df = pd.DataFrame(columns = world_table_titles)
df


# In[46]:


column_data = table.find_all('tr')


# In[47]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    

    length = len(df)
    df.loc[length] = individual_row_data 
    
    


# In[48]:


df


# In[49]:


df.to_csv(r'C:\Users\vijay\OneDrive\Desktop\Python(pandas)\Companies.csv', index = False)


# In[ ]:




