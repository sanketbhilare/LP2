#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# In[2]:


folder = './aclImdb'


# In[3]:


labels = {'pos': 1, 'neg': 0}


# In[4]:


df = pd.DataFrame()


# In[5]:


for f in ('test', 'train'):    
    for l in ('pos', 'neg'):
        path = os.path.join(folder, f, l)
        for file in os.listdir (path) :
            with open(os.path.join(path, file),'r', encoding='utf-8') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]],ignore_index=True)

df.columns = ['review', 'sentiment']


# In[6]:


df.to_csv('movie_data.csv',index=False,encoding='utf-8')


# In[7]:


df.head()


# In[8]:


reviews = df.review.str.cat(sep=' ')

#function to split text into word
tokens = word_tokenize(reviews)

vocabulary = set(tokens)
print(len(vocabulary))

#frequency_dist = nltk.FreqDist(tokens)
#sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]


# In[9]:


stop_words = set(stopwords.words('english'))
tokens = [w for w in tokens if not w in stop_words]


# In[10]:


#Stemming
stemmer=PorterStemmer()
tokens=[stemmer.stem(word) for word in tokens]


# In[11]:


#Dividing dataset into test and train

X_train = df.loc[:24999, 'review'].values
y_train = df.loc[:24999, 'sentiment'].values
X_test = df.loc[25000:, 'review'].values
y_test = df.loc[25000:, 'sentiment'].values


# In[12]:


#Using TFIDF to convert text corpus to feature vectors

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)
print(train_vectors.shape, test_vectors.shape)


# In[13]:


#Import svm model
from sklearn import svm


# In[14]:


#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(train_vectors, y_train)


# In[15]:


from  sklearn.metrics  import accuracy_score
from sklearn import metrics

predicted = clf.predict(test_vectors)

print("Accuracy:",accuracy_score(y_test,predicted))
print("Precision:",metrics.precision_score(y_test, predicted))
print("Recall:",metrics.recall_score(y_test, predicted))


# In[ ]:




