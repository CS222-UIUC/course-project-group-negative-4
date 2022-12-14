import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from visualizationShortened import visualization_shortened
#import visualizationShortened

#course, tag = input("Enter Course and Tag (ex.: CS 173): ").split()
#print("Course: ", course)
#print("Tag: ", tag)
#tag = int(tag) 

#course = "CS"
#tag = 173

#print("\n PROFS 1 \n")
#print(visualizationShortened.visualization_shortened().values.tolist())

""" Warning! CSV file contains duplicates for certain professors. When I've checked manually, most professors with duplicate rows are the same. 
    But some, are different. Oh well. My code just takes the first row that shows up when there are duplicates. I make sure to check firstName and
    lastName so you don't avoid removing a name when there's a 'Chang, Kevin' and a 'Wise, Kevin' """
df = pd.read_csv('MatPlot/RMP/rmp-data-updated.csv') 


""" Function to return list of professor names like so [['Park', 'Yongjoo'], ['Chang', 'Kevin'], ['Alawini', 'Abdussalam']] """
def rmp(course="CS",tag=173):
    #profs_df = pd.DataFrame({'Primary Instructor': ['Park, Yongjoo\n(3.27)', 'Chang, Kevin C\n(3.27)', 'Alawini, Abdussalam A\n(3.27)']})
    profs_df = visualization_shortened(course,tag)   
    #profs_df = visualizationShortened.visualization_shortened()
    #print(profs_df)    

    #Convert to List = [['Park, Yongjoo'], ['Chang, Kevin C'], ['Alawini, Abdussalam A'], ['Wise, Kevin']]
    
    
    """ The issue here is a list converts the dataframe elements to a list of lists. So I have to now be careful. """
    """Edit: Nvm ffs. Creating a dataframe manually and turning into a list is apparently different than doing df = column and then turning it into a list"""
    profs_lis = profs_df.values.tolist()

    """!! Edit: Nvm ffs. Creating a dataframe manually and turning into a list is apparently different than doing df = column and then turning it into a list"""
    #Convert [['Park, Yongjoo'], ['Chang, Kevin C'], ['Alawini, Abdussalam A']]  --> ['Park, Yongjoo', 'Chang, Kevin C', 'Alawini, Abdussalam A']
    # !! flat_list = [item for sublist in profs_lis for item in sublist]
        #print(flat_list)
    flat_list = profs_lis
    #!!! Cut out \nGPA here
    flat_list = [item.split('\n')[0] for item in flat_list]
        #print(flat_list)
    #print("\n PROFS 2 \n")
    #print(flat_list)

    #Convert to ['Park, Yongjoo', 'Chang, Kevin C', 'Alawini, Abdussalam A'] --> [['Park', 'Yongjoo'], ['Chang', 'Kevin C'], ['Alawini', 'Abdussalam A']]
    split_val = [item.split(', ') for item in flat_list]
        #print(split_val)

    #Cut middle name   --> [['Park', 'Yongjoo'], ['Chang', 'Kevin'], ['Alawini', 'Abdussalam']]
    for sublist in split_val:
        sublist[1] = sublist[1].split(' ')[0]
        #print(split_val)
    return split_val




""" Funcion to calls rmp() above, where we turn [['Park', 'Yongjoo'], ['Chang', 'Kevin'], ['Alawini', 'Abdussalam']] into a dataframe {tFname,tLname, tid,overall_rating} """
def iloc(course="CS",tag=173):
    """ Create empty_df so I can add rows in the for loop """
    empty_df = pd.DataFrame(columns=['tDept', 'tSid', 'institution_name', 'tFname',	'tMiddlename', 'tLname', 'tid',	'tNumRatings',	'rating_class', 'contentType', 'categoryType', 'overall_rating']) #empty dataframe
    
    prof_list = rmp(course, tag)
    for names in prof_list:
            lastName = names[0]
            firstName = names[1]
            df_name = df.loc[(df['tLname'] == lastName) & (df['tFname'] == firstName)]
            empty_df = pd.concat([empty_df, df_name])
            #print(df_name)
            #df3 = df2.iloc[:,[21,7,8,9,10,11,12,13,14,15,16,17,18,19,20]] 
    #print(empty_df)
    
    """ Cut out useless columns """
    iloc_df = empty_df.iloc[:,[3,5,6,11]] 
    #print(iloc_df)
    
    """ Get rid of duplicate entries and keep the first one """
    final_df = iloc_df.drop_duplicates(subset=['tFname', 'tLname'], keep='first')
    
    base_link = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid='
    final_df['Link'] = base_link + final_df['tid'].astype(str)
     
    final_df.drop('tid', axis=1, inplace=True)
    final_df.rename(columns={'tFname': 'FirstName', 'tLname': 'LastName', 'overall_rating': 'Rating'}, inplace=True)
    #print(final_df)
    return final_df

#print(iloc())
def getRMPTable(course="CS", tag=173):
    return iloc(course, tag).to_html(classes='table table-stripped',render_links=True,justify='center', index=False)
#print(result)
        
#print(getRMPTable())
        
""" Reddit Stuff"""

def reddit(course="CS",tag=173):

    """ First one is for with space, second is without space. So 'STAT 410' vs. 'STAT410' """
    reddit_link_str_1 = "https://www.reddit.com/r/UIUC/search/?q=" + course + "%20" + str(tag) + "&restrict_sr=1&sr_nsfw="
    reddit_link_str_2 = "https://www.reddit.com/r/UIUC/search/?q=" + course + str(tag) + "&restrict_sr=1&sr_nsfw="
    
    str_1 = course + " " + str(tag)
    str_2 = course + str(tag)

    data = [[str_1, reddit_link_str_1], [str_2, reddit_link_str_2]]

    reddit_df = pd.DataFrame(data, columns=['Searched Query', 'Reddit Link'])
    
    return reddit_df.to_html(classes='table table-stripped',render_links=True,justify='center', index=False)


#print(reddit("STAT", 410))

