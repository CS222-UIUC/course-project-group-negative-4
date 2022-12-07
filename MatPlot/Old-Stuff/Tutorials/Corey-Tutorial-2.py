
import numpy as np
import csv
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

with open('Matplot/gpa-sample.csv', 'r') as csv_file:
    """
    csv_reader = csv.DictReader(csv_file)
    #csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        if (row['Course Title'] == 'Statistics and Probability II'):
            print(row[0])

     csv_reader = csv.DictReader(csv_file)
    """


    csv_reader = csv.reader(csv_file)

    courses = []
    
    for row in csv_reader:
        if (row[5] == 'Statistics and Probability II'):
            print(row[0])
    






"""

course_counter = Counter()
    for row in csv_reader:
        course_counter.update(row)

    print(course_counter)


What the example is doing is passing in 
['HTML', 'JAVA', 'JAVASCRIPT']
['HTML', 'JAVA']

and this will return
Counter{'HTML': 2, 'JAVA': 2, 'JAVASCRIPT': 1}
"""



