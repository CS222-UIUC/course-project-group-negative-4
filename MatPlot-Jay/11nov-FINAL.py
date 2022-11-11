import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


""" Input Simulation """
course, tag = input("Enter Course and Tag (ex.: CS 173): ").split()
#print("Course: ", course)
#print("Tag: ", tag)
tag = int(tag)


""" Read in CSV """
df = pd.read_csv('MatPlot-Jay/fa-2021-only.csv')

""" Find DF in CSV"""
df2 = df.loc[(df['Subject'] == course) & (df['Number'] == tag)]
print(df2)
df3 = df2.iloc[:,[21,7,8,9,10,11,12,13,14,15,16,17,18,19,20]]
print(df3)



""" Now Build Visualization """
# load dataset
#df = pd.read_csv('Matplot/stat400normal.csv')
df = df3.copy()
#print(df)

my_colors = ['green', 'forestgreen', 'mediumseagreen', 
            'skyblue', 'lightskyblue', 'lightblue',
            'indianred', 'salmon', 'lightcoral',
            'wheat', 'moccasin', 'papayawhip',
            'dimgray', 'slategray']

df_total = df["A+"] + df["A"] + df["A-"] + df["B+"] + df["B"] + df["B-"] + df["C+"] + df["C"] + df["C-"] + df["D+"] + df["D"] + df["D-"] + df["F"] + df["W"]
df_rel = df[df.columns[1:]].div(df_total, 0)*100 #again, df[df.columns[1:]] is same as above, its basically the table. Then df_total is the column of the totals. I don't get the 0.
df_rel_copy = df_rel.copy() #for some reason if you try def_rel_copy = def_rel_copy it messes up below. I think it does a deep copy for some reason
df_rel_copy.insert(0, "Primary Instructor", df["Primary Instructor"])
df_rel_copy = df_rel_copy.round(2) #round to 2 decimals
#print(df_rel_copy)

df_rel_copy.plot(
    x = ('Primary Instructor'),
    kind = 'barh',
    stacked = True,
    title = course + str(tag),
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
plt.title(course + " " + str(tag), fontsize=14, pad=15)
plt.ylabel("Instructors", fontsize=10, labelpad=15)
plt.show()