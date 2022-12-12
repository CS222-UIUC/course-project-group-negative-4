import csv

#tutorial: https://www.youtube.com/watch?v=q5uM4VKywbA&ab_channel=CoreySchafer

#csv reader
with open('Matplot/gpa-sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        """
        if (line[4] == '410'): 
            print(line)
        print(line)
        """

#csv writer



#python3 ./Matplot/csv-reader.py