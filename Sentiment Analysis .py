#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


df=pd.read_csv(r"C:\Users\DELL\Desktop\Projects\sentiment\train.csv",encoding="latin1")


# In[11]:


df.isnull().sum()


# In[13]:





# In[14]:


df


# In[15]:


df['Time of Tweet'].value_counts()


# In[51]:


sentiment_count=df['sentiment'].value_counts()


# In[24]:


df[df['sentiment'] == 'negative'].groupby('Country').size().idxmax()


# In[25]:


df[df['sentiment'] == 'positive'].groupby('Country').size().idxmax()


# In[26]:


df[df['sentiment'] == 'neutral'].groupby('Country').size().idxmax()


# In[28]:


Top10_Negative=df[df['sentiment'] == 'negative']['Country'].value_counts().head(10)


# In[31]:


Top10_Positive=df[df['sentiment'] == 'positive']['Country'].value_counts().head(10)


# In[35]:


Top10_Neutral=df[df['sentiment'] == 'neutral']['Country'].value_counts().head(10)


# In[37]:


sentiment_by_time=df.pivot_table(index="Time of Tweet", columns="sentiment", aggfunc="size", fill_value=0)


# In[39]:


Tweet_with_AgeGroup=df['Age of User'].value_counts()


# In[40]:


Tweet_with_AgeGroup.plot(kind="bar", figsize=(10,5), colormap="viridis")

plt.title("Number of Tweets by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)
plt.show()


# In[49]:


sentiment_by_time.plot(kind="bar", figsize=(10,5))

plt.title("Sentiment Tweets by Time")
plt.xlabel("TimeLine")
plt.ylabel("Number Of Tweet")
plt.xticks(rotation=0)
plt.show()


# In[50]:


Top10_Negative.plot(kind="bar", figsize=(10,5))

plt.title("Top 10 country with Negative tweets")
plt.xlabel("Country")
plt.ylabel("Number of Tweets")
plt.xticks(rotation=0)
plt.show()


# In[54]:


sentiment_count.plot(
    kind="pie",
    autopct='%1.1f%%',  
    startangle=90)  
    


# In[56]:


plt.figure(figsize=(10,6))

sns.boxplot(x=df['sentiment'], y=df['Density (P/Km²)'], palette="coolwarm")

plt.title("Distribution of Population Density Across Sentiments")
plt.xlabel("Sentiment")
plt.ylabel("Population Density (P/Km²)")
plt.yscale('log')  
plt.grid(True, linestyle="--", alpha=0.6)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




