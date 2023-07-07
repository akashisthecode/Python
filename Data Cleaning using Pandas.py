#!/usr/bin/env python
# coding: utf-8

# # Importig Library

# In[4]:


import pandas as pd


# # Reading excel file in python

# In[5]:


df = pd.read_excel(r"C:\Users\Akash Mishra\Downloads\Customer Call List.xlsx")
df


# # Dropping Duplicates

# In[6]:


df=df.drop_duplicates()


# # Dropping Unrelated columns

# In[7]:


df=df.drop(columns = 'Not_Useful_Column')


# # Removing unrelated identifiers from Last_name

# In[5]:


df['Last_Name'].str.strip("123._/")


# # Removing identifiers from middle of a number

# In[16]:


df['Phone_Number']= df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')


# # Converting Phone_Number to a String format

# In[8]:


df['Phone_Number']=df['Phone_Number'].apply(lambda x: str(x))


# # Changing format of a Phone_Number

# In[21]:


df['Phone_Number'].apply(lambda x: x[0:3]+'-'+x[3:6]+'-'+x[6:10])


# In[33]:


df['Phone_Number']


# # Replacing unrelated items from Phone_Number

# In[34]:


df['Phone_Number']=df['Phone_Number'].replace('nan--','')


# In[35]:


df['Phone_Number']=df['Phone_Number'].replace('nan','')
df['Phone_Number']=df['Phone_Number'].replace('Na','')


# In[36]:


df['Phone_Number']


# In[37]:


df


# # Split Address Column into 3 different columns

# In[39]:


df[['street_address','state','zip']]= df['Address'].str.split(',',2,expand=True)


# In[40]:


df


# # Drop Address Column

# In[41]:


df.drop(columns = 'Address')


# # Replacing Yes and No values with 'Y' , 'N'

# In[46]:


df['Paying Customer']=df['Paying Customer'].replace('Yes','Y')


# In[49]:


df['Paying Customer']=df['Paying Customer'].replace('No','N')


# In[50]:


df


# In[63]:


df['Do_Not_Contact']=df['Do_Not_Contact'].replace('Yes','Y')


# In[64]:


df['Do_Not_Contact']=df['Do_Not_Contact'].replace('No','N')


# In[57]:


df= df.fillna('')


# In[58]:


df = df.replace('N/a','')


# In[65]:


df


# # Removing Do_Not_contact items from table where value is "Y"

# In[66]:


for x in df.index:
    if df.loc[x,'Do_Not_Contact']=='Y':
        df.drop(x,inplace=True)


# In[67]:


df


# # Removing Phone_Number items from list where it is blank

# In[68]:


for x in df.index:
    if df.loc[x,'Phone_Number']=='':
        df.drop(x,inplace=True)


# In[69]:


df


# # Resetting Index_Number of a table

# In[72]:


df=df.reset_index(drop=True)


# In[73]:


df


# In[ ]:




