from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from random import shuffle
import random
import csv
data11 = pd.read_csv('data_set/imdb1.txt', sep=",", header = None,error_bad_lines=False)
data11.columns = ["movie_name", "gener", "year", "rating"]

data12 = pd.read_csv('data_set/imdb2.txt', sep=",", header = None,error_bad_lines=False)
data12.columns = ["movie_name", "gener", "year", "rating"]
#data12
data13 = pd.read_csv('data_set/imdb3.txt', sep=",", header = None,error_bad_lines=False)
data13.columns = ["movie_name", "gener", "year", "rating"]
data14 = pd.read_csv('data_set/imdb4.txt', sep=",", header = None,error_bad_lines=False)
data14.columns = ["movie_name", "gener", "year", "rating"]
#data14
data15 = pd.read_csv('data_set/imdb5.txt', sep=",", header = None,error_bad_lines=False)
data15.columns = ["movie_name", "gener", "year", "rating"]
#data15
value_list=['Horror', 'Drama', 'Comedy', 'Action', 'Biography', 'Crime',
       'Thriller', 'Adventure', 'Family', 'Animation', 'Mystery', 'Sci-Fi',
       'Fantasy', 'Western', 'Romance', 'Music',  'War', 'Musical', 'History']
y_11 =[]
for i in value_list:
    s= []
    s.append(i)
    i = data11[data11.gener.isin(s)]
    y_11.append(i)
m =[]
for j in range(len(value_list)):
    k = y_11[j]["rating"].mean()
    m.append(k)
y_12 =[]
for i in value_list:
    s= []
    s.append(i)
    i = data12[data12.gener.isin(s)]
    y_12.append(i)
m_12 =[]
for j in range(len(value_list)):
    k = y_12[j]["rating"].mean()
    m_12.append(k)
y_13 =[]
for i in value_list:
    s= []
    s.append(i)
    i = data13[data13.gener.isin(s)]
    y_13.append(i)
m_13 =[]
for j in range(len(value_list)):
    k = y_13[j]["rating"].mean()
    m_13.append(k)

y_14 =[]
for i in value_list:
    s= []
    s.append(i)
    i = data14[data14.gener.isin(s)]
    y_14.append(i)
m_14 =[]
for j in range(len(value_list)):
    k = y_14[j]["rating"].mean()
    m_14.append(k)

y_15 =[]
for i in value_list:
    s= []
    s.append(i)
    i = data15[data15.gener.isin(s)]
    y_15.append(i)
m_15 =[]
for j in range(len(value_list)):
    k = y_15[j]["rating"].mean()
    m_15.append(k)
def rec_movie(gen_user,year):
    try:
        top_five=[]
    	#for i in range(len(gener)):
   	value_list_index = value_list.index(gen_user)
    	if year=="2015":
         		top_five = y_15[value_list_index]
         		top_five  = top_five.loc[random.sample(list(top_five.index),2)]
       	#top_five =  y_14[value_list_index].sort('rating', ascending=False).head(5)
    	elif year=="2013":
         		top_five = y_13[value_list_index]
         		top_five  = top_five.loc[random.sample(list(top_five.index),2)]
   	elif year=="2012":
       		        top_five = y_12[value_list_index]
        		top_five  = top_five.loc[random.sample(list(top_five.index),2)]
    	elif year=="2011":
        		top_five = y_11[value_list_index]
        		top_five  = top_five.loc[random.sample(list(top_five.index),2)]
    	elif year=="2014":
         		top_five = y_14[value_list_index]
         		top_five  = top_five.loc[random.sample(list(top_five.index),2)]

    	else:
        		print "Year is not in Range 2011-2015 !!!"
    	return top_five
    except:
	pass 
	

def calculate(main_list):
		gener = main_list
		csv_columns = ["Movie Name","Gener","Year of Release","Rating"]
		f = open('data.csv', 'wb')
		w = csv.writer(f,dialect='excel',delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
		w.writerow(csv_columns)
		f.close()
    		#recomended_movie=[]
		for gen_user in gener:
    			f = open('data.csv', 'ab')
			print gen_user
			year_list = ["2015","2014","2013","2012","2011"]
			year = random.choice(year_list)
    			a = rec_movie(gen_user,year)
    			try:
				a.to_csv(f,index=False,header = None)
				f.close()
			except:
				pass

#main_list = ["Music"]
#year_list = ["2015","2014","2013","2012","2011"]
#year = random.choice(year_list)
#calculate(main_list)
