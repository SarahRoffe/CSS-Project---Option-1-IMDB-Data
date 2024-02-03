#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:58:36 2024

@author: Sarah Roffe
"""

# Using Pandas, use the "movie_dataset.csv" found in the "Week 1" section of Canvas.

import pandas as pd

# pandas is not quite suited for large data...

movies = pd.read_csv("/home/user/Day_on_of_slaying_the_python/data_01/movie_dataset.csv") 
#/home/user/Day_on_of_slaying_the_python/data_01/movie_dataset.csv
#search abs path of data in files > right click > abs path
print(movies)

url = "https://github.com/SarahRoffe/CSS-Project---Option-1-IMDB-Data/blob/main/movie_dataset.csv"
movies = pd.read_csv(url)
# you can also use a link woohoo
# R and python are so similar

pd.set_option('display.max_columns', None) # display all col names to see which to rename
print(movies.describe())


# Clean the dataset
"""
Note, some column names have spaces which is not ideal. 
Some columns have missing values and it would be best to either fill or 
drop where appropriate those missing values to prevent a bias.
"""

# First fix the columns - remove the spaces
movies.rename(columns={"Runtime (Minutes)": "Runtime_Minutes", "Revenue (Millions)": "Revenue_Millions"}, inplace=True)

movies

movies.isna().sum() # how many nan rows??
"""
Rank                  0
Title                 0
Genre                 0
Description           0
Director              0
Actors                0
Year                  0
Runtime_Minutes       0
Rating                0
Votes                 0
Revenue_Millions    128
Metascore            64
"""

# Remove na rows
movies_dropped_na = movies.dropna()

"""
A better way to remove na
movies.dropna(inplace = True)
movies = movies.reset_index(drop=True)

Though this gives the same output as above so no biggy
"""

print(movies_dropped_na)
movies_dropped_na.isna().sum()
#no nan values
"""
Rank                0
Title               0
Genre               0
Description         0
Director            0
Actors              0
Year                0
Runtime_Minutes     0
Rating              0
Votes               0
Revenue_Millions    0
Metascore           0
dtype: int64
"""

# movies_dropped_na is the df to work with....


# Q's

# Q1
# What is the highest rated movie in the dataset? 
# result to be max(Rating) & list title...

print(movies_dropped_na['Rating'].max())
# highest rating is 9

print(movies_dropped_na.query('Rating==9')['Title'])
# answer is the dark night 

# Q2
# What is the average revenue of all movies in the dataset? 
print(movies_dropped_na["Revenue_Millions"].mean())
# 84.56455847255368

# Q3
# What is the average revenue of movies from 2015 to 2017 in the dataset?

print(movies_dropped_na['Year'].unique()) # list unique years
#[2014 2012 2016 2011 2015 2008 2006 2007 2009 2010 2013]
#no 2017 so ignore 2017

#define years
values = [2015, 2016]

#drop rows that don't contain any value in the list
movies_dropped_na_and_yrs = movies_dropped_na[movies_dropped_na.Year.isin(values) == True]

print(movies_dropped_na_and_yrs['Year'].unique()) # check your working

ave_revenue_2015_2017 = movies_dropped_na_and_yrs["Revenue_Millions"].mean()
print(ave_revenue_2015_2017)
#64.49895765472316

# Q4
# How many movies were released in the year 2016? 

values.remove(2015)
print(values)

movies_2016 = movies_dropped_na[movies_dropped_na.Year.isin(values) == True]

print(movies_2016['Year'].unique()) # check your working

len(movies_2016)
# 198
#answer is 297 if movies (not cleaned is used)
# but yours is wrong....
# works with movies - no clue why hmmmm

movies_2016 = movies[movies.Year.isin(values) == True]

print(movies_2016['Year'].unique()) # check your working

len(movies_2016)


# Q5
# How many movies were directed by Christopher Nolan? 
# do a count with director == Christopher Nolan
CN_directed = movies_dropped_na[movies_dropped_na['Director'] == 'Christopher Nolan']
len(CN_directed)
# five

# Q6
# How many movies in the dataset have a rating of at least 8.0?
Eight_rating_more = movies_dropped_na[movies_dropped_na['Rating'] >= 8.0]
len(Eight_rating_more)
# 70 - not an answer


Eight_rating_more = movies[movies['Rating'] >= 8.0]
len(Eight_rating_more)
# 78 - an answer
# Seems the na dropping is not lekker

# Q7
# What is the median rating of movies directed by Christopher Nolan? 
print(CN_directed) #df to use
print(CN_directed['Rating'].median())
# 8.6


# Q8
# Find the year with the highest average rating? 
# Ave per year grouped - then get max
grpd_rating = movies_dropped_na.groupby(['Year'],as_index=False).Rating.mean()
print(grpd_rating)
"""
Year    Rating
0   2006  7.143902 #answer
1   2007  7.140909
2   2008  6.708333
3   2009  6.911111
4   2010  6.894737
5   2011  6.945614
6   2012  6.933871
7   2013  6.832143
8   2014  6.822581
9   2015  6.674312
10  2016  6.644444
"""

# and with the original movies dataset
grpd_rating = movies.groupby(['Year'],as_index=False).Rating.mean()
print(grpd_rating)

"""
print(grpd_rating)
    Year    Rating
0   2006  7.125000
1   2007  7.133962 #answer
2   2008  6.784615
3   2009  6.960784
4   2010  6.826667
5   2011  6.838095
6   2012  6.925000
7   2013  6.812088
8   2014  6.837755
9   2015  6.602362
10  2016  6.436700
"""

# Both 2006 and 2007 are answers so assume a failure
# Take 2006...

# Q9
# What is the percentage increase in number of movies made between 2006 and 2016? 
# Cal no movies each yr and cal % inc
"""
To calculate the percentage increase:

    First: work out the difference (increase) between the two numbers you are comparing.
    Increase = New Number - Original Number.
    Then: divide the increase by the original number and multiply the answer by 100.
    % increase = Increase ÷ Original Number × 100.
"""


print(len(movies_dropped_na))
# 838 movies in tot

movies_sum_pyr = movies_dropped_na.groupby(['Year'],as_index=False).Rank.count()
print(movies_sum_pyr) # how many movies per year
"""
Year  Rank
0   2006    41
1   2007    44
2   2008    48
3   2009    45
4   2010    57
5   2011    57
6   2012    62
7   2013    84
8   2014    93
9   2015   109
10  2016   198


Tot = 838
"""

amt_inc = 198 - 41
print(amt_inc) # 157 inc
per_inc = 157 / 41 * 100
print(per_inc)
#382.9268292682927
# Again not the answer :|

print(len(movies))
# 1000 movies without removing na

movies_sum_pyr_na = movies.groupby(['Year'],as_index=False).Rank.count()
print(movies_sum_pyr_na) # how many movies per year
"""
Year  Rank
0   2006    44
1   2007    53
2   2008    52
3   2009    51
4   2010    60
5   2011    63
6   2012    64
7   2013    91
8   2014    98
9   2015   127
10  2016   297

Tot = 1000
"""

amt_inc_ = 297 - 44
print(amt_inc_) # 253 inc
per_inc_ = 253 / 44 * 100
print(per_inc_)
#575.0

# Q10
# Find the most common actor in all the movies?
#Note, the "Actors" column has multiple actors names. 
#You must find a way to search for the most common actor in all the movies.
# Split column based with splitter as comma???

Actors = movies_dropped_na[['Actors']].copy()
print(Actors)

# Split text into a list
# Then sum of unique actors...
Actors['Actors'] = Actors['Actors'].str.split(',')

# Convert list into multiple rows
Actors = Actors.explode('Actors')
print(Actors)
#Actors_unique = Actors['Actors'].unique() # some 1986 unique actors hmmmmm
#print(Actors_unique)

Actors['count'] = 1 # lets get count by actor

grouped = Actors.groupby('Actors') #defined a wee function to use later

Actors_feat_count = grouped['count'].count()
print(Actors_feat_count.info())
# Christian Bale and Mark Wahlberg - MW is answer

# Q11
#How many unique genres are there in the dataset?
#Note, the "Genre" column has multiple genres per movie. 
#You must find a way to identify them individually.

Genres = movies_dropped_na[['Genre']].copy()
print(Genres)

# Split text into a list
# Then sum of unique genres...
Genres['Genre'] = Genres['Genre'].str.split(',')

# Convert list into multiple rows
Genres = Genres.explode('Genre')
print(Genres)

Genres_unique = Genres.drop_duplicates()
print(len(Genres_unique))
# 20 unique genres...

# Q12
#Do a correlation of the numerical features, what insights can you deduce? 
#Mention at least 5 insights.
#And what advice can you give directors to produce better movies?

# What correlation??
# Pearson, spearmann, etc.??
# Say pearson for now

"""
Numerical columns:
Year
Runtime_Minutes
Rating
Votes
Revenue_Millions
Metascore  
"""

movies_dropped_na.head(10)
movies_dropped_na.tail(10) # alternative to R head() and tail() functions

corr = movies_dropped_na.corr(method = 'pearson') # don't specify cols makes it run corr for all numerical cols
print(corr) # okay so now how do I get a p value???

"""
                      Rank      Year  Runtime_Minutes    Rating     Votes  \
Rank              1.000000 -0.312809        -0.254783 -0.243125 -0.303284   
Year             -0.312809  1.000000        -0.101933 -0.145703 -0.362445   
Runtime_Minutes  -0.254783 -0.101933         1.000000  0.374566  0.399298   
Rating           -0.243125 -0.145703         0.374566  1.000000  0.517452   
Votes            -0.303284 -0.362445         0.399298  0.517452  1.000000   
Revenue_Millions -0.273170 -0.129198         0.281721  0.217106  0.636833   
Metascore        -0.195909 -0.062303         0.221397  0.672731  0.332674   

                  Revenue_Millions  Metascore  
Rank                     -0.273170  -0.195909  
Year                     -0.129198  -0.062303  
Runtime_Minutes           0.281721   0.221397  
Rating                    0.217106   0.672731  
Votes                     0.636833   0.332674  
Revenue_Millions          1.000000   0.142397  
Metascore                 0.142397   1.000000 
"""

"""
Insights - remember correlation does not equate to causation
Higher ratings and higher revenue will be key

1) Higher rating associated with higher revenue; R value is 0.22 which is a very weak strength correlation
2) Higher rating associated with longer runtime; R value is 0.37 which is a weak strength correlation
3) Higher rating associated with higher number of votes; R value is 0.52 which is a moderate strength correlation
4) Higher rating associated with higher metascore (??); R value is 0.67 which is a moderate strength correlation
5) Higher revenue associated with longer runtime; R value is 0.28 which is a very weak strength correlation
6) Higher revenue associated with higher number of votes; R value is 0.64 which is a moderate strength correlation
7) Higher revenue associated with higher metascore (??); R value is 0.14 which is a very weak correlation

"""


#OR

movies_dropped_na['Rating'].corr(movies_dropped_na['Year'])

import numpy as np
c = np.corrcoef(movies_dropped_na['Rating'],movies_dropped_na['Year']) # specify columns
# using numpy library


# corr is the file to use 
from scipy.stats import pearsonr

#calculation correlation coefficient and p-value between x and y
pearsonr(movies_dropped_na['Rating'],movies_dropped_na['Year'])
# PearsonRResult(statistic=-0.1457031775089503, pvalue=2.2939898562476055e-05)




