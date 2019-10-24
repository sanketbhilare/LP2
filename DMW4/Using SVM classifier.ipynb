{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "import nltk\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import PorterStemmer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "folder = './aclImdb'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "labels = {'pos': 1, 'neg': 0}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "for f in ('test', 'train'):    \n",
    "    for l in ('pos', 'neg'):\n",
    "        path = os.path.join(folder, f, l)\n",
    "        for file in os.listdir (path) :\n",
    "            with open(os.path.join(path, file),'r', encoding='utf-8') as infile:\n",
    "                txt = infile.read()\n",
    "            df = df.append([[txt, labels[l]]],ignore_index=True)\n",
    "\n",
    "df.columns = ['review', 'sentiment']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('movie_data.csv',index=False,encoding='utf-8')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>review</th>\n",
       "      <th>sentiment</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Based on an actual story, John Boorman shows t...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>This is a gem. As a Film Four production - the...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I really like this show. It has drama, romance...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>This is the best 3-D experience Disney has at ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Of the Korean movies I've seen, only three had...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              review  sentiment\n",
       "0  Based on an actual story, John Boorman shows t...          1\n",
       "1  This is a gem. As a Film Four production - the...          1\n",
       "2  I really like this show. It has drama, romance...          1\n",
       "3  This is the best 3-D experience Disney has at ...          1\n",
       "4  Of the Korean movies I've seen, only three had...          1"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>review</th>\n",
       "      <th>sentiment</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Based on an actual story, John Boorman shows t...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>This is a gem. As a Film Four production - the...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>I really like this show. It has drama, romance...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>This is the best 3-D experience Disney has at ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Of the Korean movies I've seen, only three had...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              review  sentiment\n",
       "0  Based on an actual story, John Boorman shows t...          1\n",
       "1  This is a gem. As a Film Four production - the...          1\n",
       "2  I really like this show. It has drama, romance...          1\n",
       "3  This is the best 3-D experience Disney has at ...          1\n",
       "4  Of the Korean movies I've seen, only three had...          1"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "198763\n",
      "198763\n"
     ]
    }
   ],
   "source": [
    "reviews = df.review.str.cat(sep=' ')\n",
    "\n",
    "#function to split text into word\n",
    "tokens = word_tokenize(reviews)\n",
    "\n",
    "vocabulary = set(tokens)\n",
    "print(len(vocabulary))\n",
    "\n",
    "#frequency_dist = nltk.FreqDist(tokens)\n",
    "#sorted(frequency_dist,key=frequency_dist.__getitem__, reverse=True)[0:50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "stop_words = set(stopwords.words('english'))\n",
    "tokens = [w for w in tokens if not w in stop_words]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Stemming\n",
    "stemmer=PorterStemmer()\n",
    "tokens=[stemmer.stem(word) for word in tokens]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dividing dataset into test and train\n",
    "\n",
    "X_train = df.loc[:24999, 'review'].values\n",
    "y_train = df.loc[:24999, 'sentiment'].values\n",
    "X_test = df.loc[25000:, 'review'].values\n",
    "y_test = df.loc[25000:, 'sentiment'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(25000, 73822) (25000, 73822)\n",
      "(25000, 73822) (25000, 73822)\n"
     ]
    }
   ],
   "source": [
    "#Using TFIDF to convert text corpus to feature vectors\n",
    "\n",
    "from sklearn.feature_extraction.text import TfidfTransformer\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "\n",
    "vectorizer = TfidfVectorizer()\n",
    "train_vectors = vectorizer.fit_transform(X_train)\n",
    "test_vectors = vectorizer.transform(X_test)\n",
    "print(train_vectors.shape, test_vectors.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Import svm model\n",
    "from sklearn import svm\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "  decision_function_shape='ovr', degree=3, gamma='auto_deprecated',\n",
       "  kernel='linear', max_iter=-1, probability=False, random_state=None,\n",
       "  shrinking=True, tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "  decision_function_shape='ovr', degree=3, gamma='auto_deprecated',\n",
       "  kernel='linear', max_iter=-1, probability=False, random_state=None,\n",
       "  shrinking=True, tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Create a svm Classifier\n",
    "clf = svm.SVC(kernel='linear') # Linear Kernel\n",
    "\n",
    "#Train the model using the training sets\n",
    "clf.fit(train_vectors, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 0.8806\n",
      "Precision: 0.8880822253038584\n",
      "Recall: 0.87096\n",
      "Accuracy: 0.8806\n",
      "Precision: 0.8880822253038584\n",
      "Recall: 0.87096\n"
     ]
    }
   ],
   "source": [
    "from  sklearn.metrics  import accuracy_score\n",
    "from sklearn import metrics\n",
    "\n",
    "predicted = clf.predict(test_vectors)\n",
    "\n",
    "print(\"Accuracy:\",accuracy_score(y_test,predicted))\n",
    "print(\"Precision:\",metrics.precision_score(y_test, predicted))\n",
    "print(\"Recall:\",metrics.recall_score(y_test, predicted))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
