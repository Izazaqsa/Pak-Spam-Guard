#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 
import matplotlib as plt 
import seaborn as sns 


# In[29]:


path = "D:/Data Science/Git Hub/Pak-Spam-Guard/expanded_pakistan_spam_dataset_10k.csv"
spamdf = pd.read_csv(path)
spamdf.head ()


# In[30]:


spamdf.isnull().sum()
spamdf.info()


# In[31]:


columns_to_drop = ['id','scam_type','language']
spamdf = spamdf.drop(columns_to_drop, axis=1)
spamdf.head()


# In[32]:


# now going to drop the url_present and url_harmful colmns also because it does not have such an impact
spamdf = spamdf.drop (['url_present','url_harmful'],axis=1)
spamdf.head()


# In[33]:


spamdf.head()


# In[34]:


spamdf.isnull().sum()
spamdf = spamdf.rename(columns={"spam":"is_spam"})
spamdf["is_spam"] = spamdf['is_spam'].map({"spam":1,'ham':0})


# In[35]:


# now applying the countvectorizer method to convert the text into numeric data 
from sklearn.feature_extraction.text import CountVectorizer
splitter = CountVectorizer()
input_data = splitter.fit_transform(spamdf.text)


# In[36]:


input_df = pd.DataFrame(input_data.toarray(),columns=splitter.get_feature_names_out())
input_df.head()


# In[37]:


# now merging both of the dataframe
spamdf= spamdf.reset_index(drop=True)
input_df = input_df.reset_index(drop=True)
spam_final_df = pd.concat([input_df,spamdf], axis=1)
spam_final_df.head()


# In[38]:


spam_final_df= spam_final_df.drop ('text',axis=1)


# In[39]:


spam_final_df.head()


# In[40]:


from sklearn.model_selection import train_test_split
x = spam_final_df.drop('is_spam',axis=1)
y = spam_final_df.is_spam
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)


# In[41]:


# now importing the algorthem 
from sklearn.naive_bayes import BernoulliNB
classifier = BernoulliNB()


# In[42]:


# hypertunning for the model 
from sklearn.model_selection import GridSearchCV
parameters = {
    'alpha': [0.001, 0.01, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0],
    'binarize': [0.0, None],
    'fit_prior': [True, False]
    }
detector = GridSearchCV(classifier,parameters)
detector.fit(x_train,y_train)


# In[44]:


training_score = detector.score(x_train,y_train)
testing_score = detector.score(x_test,y_test)
print(f"The training score is : {training_score}\nThe testing score is : {testing_score}")


# In[45]:


# also let see what are the best parameters that are selected 
print (detector.best_params_)


# In[ ]:


import pickle
with open ('splitter.pkl','wb') as vectorizer : 
    pickle.dump(splitter,vectorizer)

with open ('detector.pkl','wb') as model:
    pickle.dump(detector,model)


