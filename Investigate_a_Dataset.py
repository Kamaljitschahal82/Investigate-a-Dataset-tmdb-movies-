
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Before submitting your project, it will be a good idea to go back through your report and remove these sections to make the presentation of your work as tidy as possible. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: Investigate a Dataset (tmdb-movies)
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
# > **Tip**: 
# This data set contains information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue.
# 
#     Certain columns, like ‘cast’ and ‘genres’, contain multiple values separated by pipe (|) characters.
#     There are some odd characters in the ‘cast’ column. 
#     The final two columns ending with “_adj” show the budget and revenue of the associated movie in terms of 2010 dollars, accounting for inflation over time.
#     
#     ## questions : 
#     
#     
#     What kinds of properties are associated with movies that have high revenues?
#     -revenue over years ?
#     -popularity over years ?
#     -vote average over years ?
#     
#     effective Plots :
#     
#     -revenue vs runtime
#     -revenue vs budget 
#     -revenue vs popularity 
#     -revenue vs vote count 
#     -revenue vs vote averages 
#     -popularity vs vote counts 
#     - popularity vs vote averages
#     

# In[206]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.
import pandas as pd 
import numpy as np
from io import StringIO
from datetime import datetime
import csv
import requests
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from pandas.plotting import scatter_matrix
url="https://d17h27t6h515a5.cloudfront.net/topher/2017/October/59dd1c4c_tmdb-movies/tmdb-movies.csv"
s=requests.get(url).text
df=pd.read_csv(StringIO(s))
# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html


# In[207]:


# display 5 rows of data
df.head()


# In[208]:


# unique values count in each column 
df.nunique()


# In[209]:


# dataset column and datatype and non null value info .
df.info()


# In[210]:


# count of unique values for vote average values 
df['vote_average'].value_counts()


# In[211]:


# count of unique values for run time values 
df['runtime'].value_counts()


# In[212]:


## sum of count of unique values for vote average values 
df['vote_count'].value_counts()


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you document your steps carefully and justify your cleaning decisions.
# 
# ### General Properties
# Following issues noticed so far : 
# 1. release date is object data type ( need to convert into datetime)
# 2. release year is object datatype ( need to convert into datetime)
# 3. only 1 duplicated row .
# 4. cast & genre column have muliple values separated by PIPE characters .
# 5. Homepage , production_companies , tagline ,keywords ,imdb_id,cast,director,overview,genres have many null values        
#             
# using commands df.head() , df.info(),df.unique(),df.shape() ,sum(df.duplicated())

# In[213]:


# Load first 5 rows of the  data and print out.
df.head()


# In[214]:


# find the unique values counts in each columns .
df.nunique()


# In[215]:


# check the datatpes , null rows and non null values in each field .
df.info()


# In[216]:


# find duplicated row counts
sum(df.duplicated())


# > **Tip**:
# ### Data Cleaning (Replace this with more specific notes!)
# 1. dropped duplicate row using command df.drop_duplicates(inplace=True)
# 2. dropped null imdb_id rows using command df.dropna(subset=['imdb_id'], inplace=True)

# In[217]:


# After discussing the structure of the data and any problems that need to be
#   cleaned, perform those cleaning steps in the second part of this section.

# droping duplicate row 
df.drop_duplicates(inplace=True)


# In[218]:


sum(df.duplicated())


# In[219]:


#Any row in the data set is empty ?
df.isnull().sum().any()


# In[220]:


# checking the count of rows with null in respective columns .
df.isnull().sum()


# In[221]:


# dropping rows having null values because they are significant .
df.dropna(subset=['imdb_id'], inplace=True)


# In[222]:


# checking dropped rows cleared up from imdb_id
df.isnull().sum()


# In[223]:


# there are quite many fields with null values but we would like to keep it as our interest is to 
#trend runtime , popularity , release_date=year , revenue_adj ,vote_count  vote_average etc and each of them 10855 rows.complete data set .
df.info()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that you posed in the Introduction section. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables.
# 
# ### Research Question 1 (popular runtime , popularity and revenue over years)

# In[224]:


# Use this, and more code cells, to explore your data. Don't forget to add
#   Markdown cells to document your observations and findings.
#Exploratory Data Analysis - checking the hist trends for each individual variables.
df.hist(figsize=(10,10));


# In[225]:


# to check the trends over years group by - makes the task easier .
df = df.groupby('release_year').mean()


# In[226]:


df.hist(figsize=(10,10));


# In[227]:


scatter_matrix(df,figsize=(12,12));
plt.show();


# In[228]:


df['runtime'].describe()


# In[229]:


# describe command showing 105.71 and 107.59 (75% values)for runtime popularity , similar to as plot function 
# distribution is skewed to right 

df['runtime'].hist(bins=30)
plt.xlabel('Runtime')
plt.ylabel('Counts')
plt.title('Runtime-Years');


# In[230]:


df['popularity'].describe()


# In[231]:


df['popularity'].hist(bins=30)
plt.xlabel('Popularity')
plt.ylabel('Counts')
plt.title('Popularity-Years');


# # 0.73-0.8 , 0.35-0.40 - no values .
# # dist is right skewed .
# # highest around 0.59
# # max ratings are on lowered between 0.46 & 0.62

# In[233]:



df['revenue'].describe()


# In[234]:


df['revenue'].hist(bins=30)
plt.xlabel('Revenue')
plt.ylabel('Counts') # typical revenue earned per movie 
plt.title('Revenue-Years');


# # Dist is left skewed.
# #Revenues widely spread out 
# #Most movie revenues fall in the 3.7e+07 to 4.8e+07 ranges.
# #lower revenue on 0 - 3 range 

# In[235]:



df['vote_average'].describe()


# In[236]:


df['vote_average'].hist(bins=30)
plt.xlabel('vote_average')
plt.ylabel('Counts') # typical revenue earned per movie 
plt.title('vote_average-Years');


# # Dist is right skewed and widely spread on lower side .
# #Most average votes fall in the 5.9-6.0  ranges.
# 

# ### Research Question 2  (multiple variables analysis over years - revenue vs budget , revuenue vs runtime,revenue vs vote counts , revenue vs average counts , revenue vs popularity)

# In[237]:


# Continue to explore the data to address your additional research
#   questions. Add more headers as needed if you have more questions to

# variables associated with revenue over years ?
df.corr(method='pearson')


# # Observations from pearson correlation :
#     #revenue is correlated positively with popularity,budget and vote counts & negatively correlated with vote averages and runtime.
# 

# # scatterplot for revenue vs budget  over years

# In[238]:


plt.scatter(x=df['revenue'], y=df['budget'])
plt.xlabel('Revenue')
plt.ylabel('budget')
plt.title('Revenue vs budget - Years');


# # Observations from revenue  vs budget  over years scatterplot:
# #budget is proportional to revenues as budget gets uptick nearly high revenue.

# # scatterplot for revenue vs runtime  over years

# In[239]:


plt.scatter(x=df['revenue'], y=df['runtime'])
plt.xlabel('Revenue')
plt.ylabel('runtime')
plt.title('Revenue vs runtime - Years');


# # Observations from revenue  vs runtime over years scatterplot:
# #runtime is inversely proportional to revenues.

# # scatterplot for revenue vs votecounts  over years

# In[240]:



plt.scatter(x=df['revenue'], y=df['vote_count'])
plt.xlabel('Revenue')
plt.ylabel('Vote_Count')
plt.title('Revenue vs Vote Count - Years');


# # Observations from revenue  vs vote_counts  over years scatterplot:
# 
# #Vote count is proportional to revenues as high vote counts nearly high revenue.

# # scatterplot for revenue vs popularity over years

# In[241]:


plt.scatter(x=df['revenue'], y=df['popularity'])
plt.xlabel('Revenue')
plt.ylabel('Popularity')
plt.title('Revenue vs Popularity-Years');


# # Observations from revenue  vs popularity  over years scatterplot:
# #Popularity is proportional to revenues.
# 

# # scatterplot for revenue vs vote averages over years

# In[242]:


plt.scatter(x=df['revenue'], y=df['vote_average'])
plt.xlabel('Revenue')
plt.ylabel('Vote Averages')
plt.title('Revenue vs Vote Averages-Years');


# # Observations from revenue vs vote averages scatterplot:¶
# 
# #vote averages are inversely proportional to revenues & negative correlation as shown by pearson method .
# 
# #voting variables as influencing revenues
# 

# In[243]:


plt.scatter(x=df['popularity'], y=df['vote_average'])
plt.xlabel('popularity')
plt.ylabel('Vote Averages')
plt.title('popularity vs Vote Averages-Years');


# # Observations from popularity vs vote averages scatterplot:¶
# 
# #vote averages are inversely proportional to popularity & negative correlation as shown by pearson method .
# 
# #voting variables as influencing popularity
# 

# In[244]:


plt.scatter(x=df['popularity'], y=df['vote_count'])
plt.xlabel('popularity')
plt.ylabel('Vote count')
plt.title('popularity vs Vote count-Years');


# # Observations from popularity vs vote count  scatterplot:¶
# 
# #vote counts are  proportional to popularity & positive correlation as shown by pearson method .
# 
# #voting counts as influencing popularity .
# 

# # <a id='conclusions'></a>
# ## LIMITATIONS : 
# -in the analysis , we have looked into popularity ,runtime, revenue etc .
# 
# -to get votes - probably different survey questions might be depolyed as languages , region , countries can be different for different movies.
# 
# -We considered value of revenue in numbers not any currencies or exchange rate factors required  .
# 
# -Period of votes , popularity indexes can be different from places to places .
# 
# -target audience influencing the results of votes can varies from country to country.
# 
# -whether revenue generated from old or theaters , digital media etc .
# 
# - there are missing values , we ignored as he had 10855 rows for popularity , revenue , runtime,vote counts etc . 
# 
# - multiple values in cast / genre - field requires to add columns and separate out the data in new df  and then append original df to create set of visulation which - cast/ genre  is related to most popular movies.
# 
# 
# 
# 
# 
# 
# 
# 
# ## Conclusions
# 
# ## from dataset , we investigated & discovered that over the years
# 
# -105.71 and 107.59 (75% values)for runtime popularity.
# 
# -Most movie revenues fall in the 3.7e+07 to 4.8e+07 ranges.
# 
# -maximum popularity received fall in the 0.46 to 0.62 ranges.
# 
# -Most average votes fall in the 5.9-6.0 ranges
# 
# 
# ## Multiple variables 
# ## Key obeservations in our analysis,
# 
# -popularity,vote_counts ,budget are directly proportional to revenue over years .
# 
# -average votes and run time are inversely proportional to revenue over years 
# 
# - average votes are inversely proportional to popularity over years .
# 
# - vote counts are directly proportional to popularity over years .
# 
# -Probably , voting results are influencing overall results, this requires further investigation what type of survey questions or method used .
# 
# 
# ## Submitting your Project 
# 
# > Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[1]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

