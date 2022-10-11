# -*- coding: utf-8 -*-
"""Copy of Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EtlOTIaD7phwwWzSf82XcNMPApZo5S0f
"""

from IPython.core.interactiveshell import prefilter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import statistics as stat

df = pd.read_csv('/content/Enrollments_28092022.csv')
df

df.info()

rows = len(df.axes[0])
print("number of rows :",str(rows))

cols = len(df.axes[0])
print("number of columns:",str(cols))

plt.hist(df['DEGREE'])
plt.show

plt.hist(df['INTERMEDIATE'])
plt.show

plt.hist(df['SSC'])
plt.show

courses = ['Data Science','MEAN STACK WEB Development','Cloud Computing Services(AWS']
students = [156,51,90]
colors = ['c','g','y']
plt.pie(students,labels=courses,colors=colors,startangle=90,explode=(0,0,0),autopct = '%1.2f%%')
plt.axis('equal')
plt.show

df['INTERNSHIP'].value_counts()

print('DEGREE')
print("Mean=",np.mean(df['DEGREE']))
print("MEDIAN =",np.median(df['DEGREE']))
print("Mode=",stat.mode(df['DEGREE']))

print('INTERMEDIATE')
print("Mean=",np.mean(df['INTERMEDIATE']))
print("MEDIAN =",np.median(df['INTERMEDIATE']))
print("Mode=",stat.mode(df['INTERMEDIATE']))

print('SSC')
print("Mean=",np.mean(df['SSC']))
print("MEDIAN =",np.median(df['SSC']))
print("Mode=",stat.mode(df['SSC']))

cv=lambda x: np.std(x, ddof=1)/np.mean(x)*100

print('DEGREE')
print("Range=",max(df['DEGREE'])-min(df['DEGREE']))
print("Co-efficient of variation=",cv(df['DEGREE']))
df['DEGREE'].describe()

print('INTERMEDIATE')
print("Range=",max(df['INTERMEDIATE'])-min(df['INTERMEDIATE']))
print("Co-efficient of variation=",cv(df['INTERMEDIATE']))
df['INTERMEDIATE'].describe()

print('SSC')
print("Range=",max(df['SSC'])-min(df['SSC']))
print("Co-efficient of variation=",cv(df['SSC']))
df['SSC'].describe()

import scipy.stats as stats

print("stsndard scores od degree")
print(stats.zscore(df['DEGREE']))

print("stsndard scores od degree")
print(stats.zscore(df['INTERMEDIATE']))

print("stsndard scores od degree")
print(stats.zscore(df['SSC']))

plt.boxplot(df['DEGREE'])
plt.show()

plt.boxplot(df['INTERMEDIATE'])
plt.show()

plt.boxplot(df['SSC'])
plt.show()

def outlier(a):
  q1 = np.quantile(a,0.25)
  q3 = np.quantile(a,0.75)
  med = np.median(a)
  iqr = q3-q1
  upper_bound = q3+(1.5*iqr)
  lower_bound = q3-(1.5*iqr)
  print(iqr,upper_bound,lower_bound)
  print("inter quantile range:",iqr)
  outliers = a[(a<=lower_bound)| (a>=upper_bound)]
  print("the following are the outlier in boxplot:\n{}".format(outlier))

outlier(df['DEGREE'])

outlier(df['INTERMEDIATE'])

outlier(df['SSC'])

def func(b):
  q9 = np.quantile(b,0.9)
  li = b[b==q9]
  print("no.of students with 90% percentile:",li.count())

func(df['DEGREE'])

func(df['INTERMEDIATE'])

func(df['SSC'])