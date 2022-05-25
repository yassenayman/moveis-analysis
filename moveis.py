#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project:movies
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# #This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue. but if movie had a high vote and it's bad? that's mean that there are many factors to evaluate the dataset'
# 
# 
# ### Question(s) for Analysis
# the number of appearances per actor?
# how many movies had spread at that date?
# movies with higher votes count received a more ratings?
# 

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


# Upgrade pandas to use dataframe.explode() function. 
get_ipython().system('pip3 install --upgrade pandas')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# ### General Properties

# In[4]:


df=pd.read_csv('tmdb-movies.csv')
df.head()


# 
# ### Data Cleaning
# in this section we  print shape of data then we describe it and chek nulls, if there we drp it
#  After discussing the structure of the data and any problems that need to be cleaned
#  

# In[5]:



print(list(df.columns.values))
print(df.shape)
#describe
print(df.describe())
print(df.info())
#check null
data = df[df["cast"].isnull() == False]
data = df[df["genres"].isnull() == False]
#drop nulls
df.dropna(axis=0, inplace=True)


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# ### Research Question 1 #movies with higher votes count received a more ratings?
# 

# In[11]:



df_ratings = df.loc[:, 'vote_count' : 'vote_average']
df_vote = df_ratings[df_ratings['vote_count'] > 3000]
df_vote.plot(x='vote_count', y='vote_average',title='Ratings', kind='scatter');
df_ratings.plot(x='vote_count', y='vote_average',title='Ratings', kind='scatter');


# in this 2 graphs we see that the count of votes often be less than 3000 
# ### Research Question 2  # how many movies had spread at that date?

# In[7]:




df['release_date']=pd.to_datetime(df['release_date'])
show_count=df.groupby('release_date')[['id']].count()
show_count['id'].plot()
plt.ylabel('Number of films')
plt.title('num of films had been published in that years')
plt.xlabel('Release Date');



from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[27]:


actor_apperance={}
actors=df['cast'].str.split("|") 
actors=np.array(actors)
print(actors)


# In[ ]:




