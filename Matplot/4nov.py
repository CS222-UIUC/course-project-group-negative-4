import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
  
old_df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                       'points': [18, 22, 19, 14, 14, 11, 20, 28],
                       'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                       'rebounds': [11, 8, 10, 6, 6, 7, 9, 12]})

print(old_df)
  
  


# load dataset
df = pd.read_csv('Matplot/stat400normal.csv')
df = pd.read_csv('Matplot/stat400percentageconvert.csv')
  
# view dataset
print(df)
  
my_colors = ['green', 'forestgreen', 'mediumseagreen', 
            'skyblue', 'lightskyblue', 'lightblue',
            'indianred', 'salmon', 'lightcoral',
            'wheat', 'moccasin', 'papayawhip',
            'dimgray', 'slategray']
#plt.grid()
# plot a Stacked Bar Chart using matplotlib
df.plot(
    x = 'Instructor',
    kind = 'barh',
    stacked = True,
    title = 'STAT400',
    mark_right = True,
    color=my_colors)



df_total = df["A+"] + df["A"] + df["A-"] + df["B+"] + df["B"] + df["B-"] + df["C+"] + df["C"] + df["C-"] + df["D+"] + df["D"] + df["D-"] + df["F"] + df["W"]

df_rel = df[df.columns[1:]].div(df_total, 0)*100 #???


df_rel_copy = df_rel.copy()
df_rel_copy.insert(0, "Instructor", ["Yu", "Unger", "Nguyen"])
print(df_rel_copy["C+"])
print(df_rel_copy)

#???
for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, 1:].cumsum(1)[n], 
                                         df[n], df_rel[n])):
        #if (n == 'A'):
            #plt.text(cs - ab / 2, i, , va = 'center', ha = 'center')
        if (n[0] != 'C' and n[0] != 'D' and n[0] != 'F' and n[0] != 'W'):         
            plt.text(cs - ab / 2, i, n + ' ' + '(' + str(np.round(pc, 1)) + '%)', 
                    va = 'center', ha = 'center', fontsize = 5)

        
#plt.figure(figsize=(20,8))
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')

plt.show()



#Instructor,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W
#"Yu, Albert",38.95, 34.74, 5.27, 8.43, 5.27, 1.06, 1.06, 1.06, 0, 1.06, 2.11, 0, 0, 1.06
#"Unger, David",1.37, 27.4, 19.18, 6.85, 15.07, 6.85, 2.74, 6.85, 1.37, 2.74, 0, 1.37, 6.85, 1.37
#"Nguyen, Ha Khanh",3.75, 40.65, 8.56, 9.63, 7.49, 5.89, 6.42, 3.21, 2.68, 2.68, 0.54, 1.61, 5.35, 1.61


#Instructor,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W
#"Yu, Albert",37,33,5,8,5,1,1,1,0,1,2,0,0,1
#"Unger, David",1,20,14,5,11,5,2,5,1,2,0,1,5,1
#"Nguyen, Ha Khanh",7,76,16,18,14,11,12,6,5,5,1,3,10,3