import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import linear_kernel,cosine_similarity
import matplotlib
import matplotlib.pyplot as plt
df = pd.read_csv("final-job-data.csv",encoding='latin-1')
print(df.index)
print(df.columns)
features = ['job_description', 'job_title','sector']
for feature in features:
   df[feature] = df[feature].fillna('')


def combined_features(row):
   return row['job_description'] + " " + row['job_title']+ " " + row['sector']


df["combined_features"] = df.apply(combined_features, axis=1)
print(df)

cv = CountVectorizer()
count_matrix = cv.fit_transform(df["combined_features"])
print("Count Matrix:", count_matrix.toarray())
print(count_matrix.shape)


def get_title_from_index(Index):
   return df.loc[df.Index == Index]["job_title"].values[0]


def get_organization_from_index(Index):
   return df.loc[df.Index == Index]["organization"].values[0]


def get_location_from_index(Index):
   return df.loc[df.Index == Index]["location"].values[0]


def get_index_from_title(title):
   return df.loc[df['job_title'] == title]['Index'].values[0]


def recommendationjobtitle(num):
   job_title = get_title_from_index(num)
   return job_title


def recommendationjoborganization(num):
   job_organization = get_organization_from_index(num)
   return job_organization


def jobsearch(query1,query2,query3,query4):
   query = query1 + query2 + query3 + query4
   queryTFIDF = TfidfVectorizer().fit(df["combined_features"])
   datasetTFIDF = TfidfVectorizer().fit_transform(df["combined_features"])
   queryTFIDF = queryTFIDF.transform([query])
   # print(queryTFIDF.toarray())
   # print(queryTFIDF.shape)
   cosine_sim = cosine_similarity(queryTFIDF, datasetTFIDF).flatten()
   # print(cosine_sim.shape)
   # print(cosine_sim)
   related_product_indices = cosine_sim.argsort()[:-21:-1]
   # print(related_product_indices)
   # print(related_product_indices.shape)
   jobname = []
   for i in related_product_indices:
      jobname.append(recommendationjobtitle(i))
      #print(name)
      # organization = recommendationjoborganization(i)
      # print("Title---->"+name+"-----Organization---->"+organization)
   return jobname

def joborganization(query1,query2,query3,query4):
   query = query1 + query2 + query3 + query4
   queryTFIDF = TfidfVectorizer().fit(df["combined_features"])
   datasetTFIDF = TfidfVectorizer().fit_transform(df["combined_features"])
   queryTFIDF = queryTFIDF.transform([query])
   # print(queryTFIDF.toarray())
   # print(queryTFIDF.shape)
   cosine_sim = cosine_similarity(queryTFIDF, datasetTFIDF).flatten()
   # print(cosine_sim.shape)
   # print(cosine_sim)
   related_product_indices = cosine_sim.argsort()[:-21:-1]
   # print(related_product_indices)
   # print(related_product_indices.shape)
   organizationname = []
   for i in related_product_indices:
      organizationname.append(recommendationjoborganization(i))
      #print(name)
      # organization = recommendationjoborganization(i)
      # print("Title---->"+name+"-----Organization---->"+organization)
   return organizationname

#jobtitle = jobsearch("machine learning,java","software engineering","Computer Sceince and Engineer","Java")
#organization = joborganization("machine learning,java","software engineering","Computer Sceince and Engineer","Java")
'''for i in jobtitle:
   print("Title : "+i)

for i in organization:
   print("Organization Name : "+i)'''