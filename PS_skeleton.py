#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pandorable problem set 3 for PSY 3100 - Fall 2021

@author: katherineduncan

In this problem set, you'll practice your new pandas data management skills,
continuing to work with the 2018 IAT data used in class

Note that this is a group assignment. Please work in groups of ~4. You can divvy
up the questions between you, or better yet, work together on the questions to
overcome potential hurdles
"""

#%% import packages
import pandas as pd

#%%
# Question 1: reading and cleaning

# read in the included IAT_2018.csv file
IAT = ...

# rename and reorder the variables to the following (original name->new name):
# the number corresponds to the desired column index
# 0 session_id->id
# 1 genderidentity->gender
# 2 raceomb_002->race
# 3 edu->edu
# 4 politicalid_7->political
# 5 STATE -> state
# 6 att_7->attitude
# 7 tblacks_0to10-> tblack
# 8 twhites_0to10-> twhite
# 9 labels->labels
# 10 D_biep.White_Good_all->D_white_bias
# 11 Mn_RT_all_3467->rt

IAT = ...

IAT = ...

# check out the replace method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html
# use this to recode gender to be integers where 1=men and 2=women (instead of '[1]' coding for men and '[2]' for women)

# use this cleaned dataframe to answer the following questions

#%%
# Question 2: sorting and indexing

# use sorting and indexing to print out the following information:

# 2a: the ids of the 5 participants with the fastest reaction times

# 2b: the ids of the 5 men with the strongest white-good bias

# 2c: the ids of the 5 women in new york with the strongest white-good bias



#%%
# Question 3: loops and pivots

# 3a check out the unique method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html
# use it to get a list of states
states = ...

# is there anything strange in your list of states?  How might you clean this up?

# 3b: write a loop that iterates over states to calculate the median white-good 
# bias per state
# store the results in a stateBias dataframe with 2 columns: states & bias
# hint you will need to use indexing to store the median on each iteration
# I recommend using iloc
sind=0
stateBiasLoop=pd.DataFrame(states,columns=['state']) # create a dataframe to store the results
stateBiasLoop['bias']=None # add a column to store the bias, setting default to None, indicating missing data

for ... # AK = 0.482765

# 3c: now use the pivot_table function to calculate the same statistics as the above loop
stateBiasPivot = ... 

# 3d: merge the two dataframes according to state to test they have the outcomes
# be sure to automate the test so that you get a single output with one value when they are identical
# and other values when they are not (hint: you can take the mean of boolean comparisons)  
stateBias = ...