#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# In[3]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.info()


# In[4]:


dv["age"]=dv["age"]*50
dv


# In[5]:


dv["gender"].value_counts()


# In[10]:


dv


# In[11]:


dv["income"]=dv["income"]*20000
dv


# # Find the value count of different data types

# In[16]:


dv["private"].value_counts()


# In[13]:


dv["reduced"].value_counts()


# In[14]:


dv["health"].value_counts()


# In[15]:


dv["age"].value_counts()


# # Describing the info of the datatypes

# In[17]:


dv.describe()


# In[18]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.dropna(axis = 1)


# In[21]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.fillna("16")


# In[20]:


dv.ffill(axis = 1)


# In[22]:


dv.bfill(axis = 1)


# In[23]:


dv.drop_duplicates()


# In[24]:


dv.drop_duplicates(subset=['private'])


# In[25]:


dv.drop_duplicates(subset=['freerepat','illness'])


# In[26]:


dv.shape


# In[27]:


dv.columns


# In[28]:


dv.isna().sum()


# # Analyzing the variables

# In[29]:


# load libraries
import pandas as pd
dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.visits.unique()


# In[30]:


dv.gender.unique()


# In[31]:


dv.freerepat.unique()


# In[32]:


dv.private.unique()


# In[33]:


dv.nchronic.unique()


# In[34]:


dv.age.unique()


# In[35]:


dv.income.unique()


# In[36]:


dv.nunique()


# # Exploring and Plotting the data

# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[38]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# In[46]:


gender_counts = dv['gender'].value_counts()
sns.barplot(x=gender_counts.index,y=gender_counts.values)
plt.xlabel('gender')
plt.ylabel('visit')
plt.title('Distribution of Patient Gender')
plt.show()


# In[44]:


sns.histplot(dv['age'], bins=40)


# In[45]:


sns.histplot(dv['age'], bins=20)
plt.xlabel('age')
plt.ylabel('visit')
plt.title('Distribution of Patients age')
plt.show


# In[8]:


a=list(dv.income)
plt.boxplot(a)
plt.show()


# In[48]:


sns.histplot(dv['visits'], bins=30)
plt.xlabel('visits')
plt.ylabel('income')
plt.title('visit analysis')
plt.show


# # Observations

# In[53]:


labels=['visits','illness','reduced','health']
sizes=[35,18,13,9]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[56]:


x = [16,12,14,19,25]
y = [14,18,20,12,9]
plt.plot(x,y)
plt.xlabel('nchronic')
plt.ylabel('Ichronic')
plt.title('Disease analysis')
plt.show()


# In[58]:


labels=['freerepat','freepoor']
sizes=[40,60]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('patient health insurance analysis')
plt.show()


# In[60]:


labels=['visits','illness']
sizes=[60,45]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[61]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[63]:


labels=['visits','illness','reduced','health']
sizes=[40,28,18,9]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[64]:


x = [19,70,56,89,20]
y = [25,40,56,70,65]
plt.scatter(x,y)
plt.xlabel('freepoor')
plt.ylabel('private')
plt.title('insurance analysis')
plt.show()


# In[65]:


import pandas as pd
dv=pd.read_excel("DoctorVisits (2).xlsx")


# In[67]:


dv.hist(figsize=(30,26))


# In[68]:


x= (dv[['health']]==1).sum()
y= (dv[['health']]==0).sum()
percent= ((x*y)/(x+y))*100
percent


# # Conclusion
# 

# a) We analyzed the dataset which is about the visiting of patients to doctor.
# 

# b) We examined each variable in the dataset.
# In comparison to men, women are more numerous. Income has no significant impact on the dataset's consistency. Age and health conditions have a little greater impact on the analytics.

# c) Female gender is more in number comparable to male gender
# 

# d) The dataset's private information isn't used very extensively.

# e) Coming to the factor of age condition and health condition those are some what creating some kind of difference in the analytics.
# 

# f) Income doesn't create any kind of difference in the dataset it made it's consistency path asusally

# g) Many diseases are lchronic rather than nchronic.
# 
