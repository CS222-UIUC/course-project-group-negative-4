import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
  

# load dataset
df = pd.read_csv('Matplot/stat400normal.csv')
#print(df)

my_colors = ['green', 'forestgreen', 'mediumseagreen', 
            'skyblue', 'lightskyblue', 'lightblue',
            'indianred', 'salmon', 'lightcoral',
            'wheat', 'moccasin', 'papayawhip',
            'dimgray', 'slategray']

df_total = df["A+"] + df["A"] + df["A-"] + df["B+"] + df["B"] + df["B-"] + df["C+"] + df["C"] + df["C-"] + df["D+"] + df["D"] + df["D-"] + df["F"] + df["W"]
df_rel = df[df.columns[1:]].div(df_total, 0)*100 #again, df[df.columns[1:]] is same as above, its basically the table. Then df_total is the column of the totals. I don't get the 0.
df_rel_copy = df_rel.copy() #for some reason if you try def_rel_copy = def_rel_copy it messes up below. I think it does a deep copy for some reason
df_rel_copy.insert(0, "Instructor", df["Instructor"])
df_rel_copy = df_rel_copy.round(2) #round to 2 decimals
#print(df_rel_copy)

df_rel_copy.plot(
    x = ('Instructor'),
    kind = 'barh',
    stacked = True,
    title = ('STAT400'),
    mark_right = True,
    color=my_colors,
    figsize=(16, 8),
    xlim=(-2,102))

#print(df_rel)

for n in df_rel:
    for i, (cs, ab, pc) in enumerate(zip(df_rel_copy.iloc[:, 1:].cumsum(1)[n], 
                                         df_rel_copy[n], df_rel[n])):
        if (n[0] != 'C' and n[0] != 'D' and n[0] != 'F' and n[0] != 'W'):         
            plt.text(cs - ab / 2, i, n + ' ' + '(' + str(np.round(pc, 1)) + '%)', va = 'center', ha = 'center', fontsize = 6) 
        

#plt.figure(figsize=(20,8)) WHY DOESN'T THIS WORK?
plt.legend(loc='best', bbox_to_anchor=(0.96, -0.05), ncol=len(df.columns)) #loc='upper left'
plt.title("STAT400", fontsize=14, pad=15)
plt.ylabel("Instructors", fontsize=10, labelpad=15)
plt.show()




#Instructor,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W
#"Yu, Albert",38.95, 34.74, 5.27, 8.43, 5.27, 1.06, 1.06, 1.06, 0, 1.06, 2.11, 0, 0, 1.06
#"Unger, David",1.37, 27.4, 19.18, 6.85, 15.07, 6.85, 2.74, 6.85, 1.37, 2.74, 0, 1.37, 6.85, 1.37
#"Nguyen, Ha Khanh",3.75, 40.65, 8.56, 9.63, 7.49, 5.89, 6.42, 3.21, 2.68, 2.68, 0.54, 1.61, 5.35, 1.61


#Instructor,A+,A,A-,B+,B,B-,C+,C,C-,D+,D,D-,F,W
#"Yu, Albert",37,33,5,8,5,1,1,1,0,1,2,0,0,1
#"Unger, David",1,20,14,5,11,5,2,5,1,2,0,1,5,1
#"Nguyen, Ha Khanh",7,76,16,18,14,11,12,6,5,5,1,3,10,3