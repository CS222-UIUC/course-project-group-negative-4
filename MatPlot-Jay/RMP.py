import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#course, tag = input("Enter Course and Tag (ex.: CS 173): ").split()
#print("Course: ", course)
#print("Tag: ", tag)
#tag = int(tag) 

#course = "CS"
#tag = 173

df = pd.read_csv('MatPlot-Jay/rmp-data.csv')

""" Function to return list of professor names like so [['Park', 'Yongjoo'], ['Chang', 'Kevin'], ['Alawini', 'Abdussalam']] """
def rmp():
    #df = pd.read_csv('MatPlot-Jay/rmp-data.csv')
    #df3 = df.sort_values(by=['tDept'])
    df4 = df.loc[(df['tDept'] == 'Statistics')]

    profs_df = pd.DataFrame({'Primary Instructor': ['Park, Yongjoo', 'Chang, Kevin C', 'Alawini, Abdussalam A']})
    #print(profs_df)    

    #Convert to List
    profs_lis = profs_df.values.tolist()
        #print(profs_lis)

    #Convert [['Park, Yongjoo'], ['Chang, Kevin C'], ['Alawini, Abdussalam A']]  --> ['Park, Yongjoo', 'Chang, Kevin C', 'Alawini, Abdussalam A']
    flat_list = [item for sublist in profs_lis for item in sublist]
        #print(flat_list)

    #Convert to ['Park, Yongjoo', 'Chang, Kevin C', 'Alawini, Abdussalam A'] --> [['Park', 'Yongjoo'], ['Chang', 'Kevin C'], ['Alawini', 'Abdussalam A']]
    split_val = [item.split(', ') for item in flat_list]
        #print(split_val)

    #Cut middle name   --> [['Park', 'Yongjoo'], ['Chang', 'Kevin'], ['Alawini', 'Abdussalam']]
    for sublist in split_val:
        sublist[1] = sublist[1].split(' ')[0]
        #print(split_val)
    return split_val

def iloc():
    empty_df = pd.DataFrame(columns=['tDept', 'tSid', 'institution_name', 'tFname',	'tMiddlename', 'tLname', 'tid',	'tNumRatings',	'rating_class', 'contentType', 'categoryType', 'overall_rating']) #empty dataframe
    prof_list = rmp()
    #print(prof_list)
    for names in prof_list:
            lastName = names[0]
            firstName = names[1]
            df_name = df.loc[(df['tLname'] == lastName) & (df['tFname'] == firstName)]
            empty_df = pd.concat([empty_df, df_name])
            #print(df_name)
            #df3 = df2.iloc[:,[21,7,8,9,10,11,12,13,14,15,16,17,18,19,20]] 
    #print(empty_df)
    
    iloc_df = empty_df.iloc[:,[3,5,6,11]] 
    return iloc_df

print(iloc())
        
        
        
        
        
#df_test['Btime'].iloc[0]
""" if 'Alawini' in df['tLname'].values:
    print("HELLO") """