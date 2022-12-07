import requests
import json
import math
import pandas as pd
#from website.models import Professor

class RateMyProfScraper:
        def __init__(self,schoolid):
            self.UniversityId = schoolid
            self.professorlist = self.createprofessorlist()
            self.indexnumber = False

        def createprofessorlist(self):#creates List object that include basic information on all Professors from the IDed University
            tempprofessorlist = []
            num_of_prof = self.GetNumOfProfessors(self.UniversityId)
            print(num_of_prof)
            num_of_pages = math.ceil(num_of_prof / 20)
            print(num_of_pages)
            i = 1
            while (i <= num_of_pages):# the loop insert all professor into list
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    self.UniversityId)) # &filter=teacherlastname_sort_s+asc
                temp_jsonpage = json.loads(page.content)
                temp_list = temp_jsonpage['professors']
                tempprofessorlist.extend(temp_list)
                i += 1
            print("the data type of tempprofessorlist[0] is ", type(tempprofessorlist[0]))
            return tempprofessorlist

        def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page # &filter=teacherlastname_sort_s+asc
            temp_jsonpage = json.loads(page.content)
            num_of_prof = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            return num_of_prof

        def SearchProfessor(self, ProfessorName):
            self.indexnumber = self.GetProfessorIndex(ProfessorName)
            self.PrintProfessorInfo()
            return self.indexnumber

        def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def PrintProfessorInfo(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
            else:
                print(self.professorlist[self.indexnumber])

        def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
                #return "error"
            else:
                print(self.professorlist[self.indexnumber][key])
                return self.professorlist[self.indexnumber][key]


#WilliamPatersonUniversity = RateMyProfScraper(1205)
#WilliamPatersonUniversity.SearchProfessor("Cyril Ku")
#WilliamPatersonUniversity.PrintProfessorDetail("overall_rating")



        #def createprofessorlist(self):#creates List object that include basic information on all Professors from the IDed University
        #def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
        #def SearchProfessor(self, ProfessorName):
        #def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
        #def PrintProfessorInfo(self):  # print search professor's name and RMP score
        #def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
UIUC = RateMyProfScraper(1112)
print(UIUC.SearchProfessor("Albert Yu"))


# id = db.Column(db.Integer, primary_key=True)
#     tDept = db.Column(db.String(255))
#     tSid = db.Column(db.Integer) 
#     institution_name = db.Column(db.String(255))
#     tFname = db.Column(db.String(255)) 
#     tMiddlename = db.Column(db.String(255)) 
#     tLname = db.Column(db.String(255))  
#     tid = db.Column(db.Integer)  
#     tNumRatings = db.Column(db.Integer) 
#     rating_class = db.Column(db.String(255)) 
#     contentType = db.Column(db.String(255)) 
#     categoryType = db.Column(db.String(255)) 
#     overall_rating = db.Column(db.FLOAT(unsigned=True))
#new_prof = Professor(tDept=data[0].tsid, tSid=a, institution_name=a, tFname=a, tMiddlename=a, tLname=a, tid=a, tNumRating=a, rating_class=a,
#contentType=a, categoryType=a, overall_rating=a)
#df = pd.DataFrame.from_dict(data) 
#columns=['tDept', 'tSid', 'institution_name', 'tFname', 'tMiddlename', 'tLname', 'tid', 'tNumRatings','rating_class','contentType','categoryType','overall_rating'])
#print(df)
#print(data[0].tSid)

import csv

def write_dicts_to_csv_fieldnames(list_of_dicts, file_path, field_names):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file_object:
        writer = csv.DictWriter(csv_file_object, fieldnames=field_names)
        writer.writeheader()
        for row_dict in list_of_dicts:
            writer.writerow(row_dict)

field_names = ['tDept', 'tSid', 'institution_name', 'tFname', 'tMiddlename', 'tLname', 'tid', 'tNumRatings','rating_class','contentType','categoryType','overall_rating']
#data = [ {'name': 'Mickey Mouse', 'company': 'Disney', 'nemesis': 'Donald Duck'}, {'name': 'Road Runner', 'company': 'Warner Brothers', 'nemesis': 'Wile Ethelbert Coyote'} ]
data = UIUC.professorlist
path = 'rmp-data.csv'
write_dicts_to_csv_fieldnames(data, path, field_names)

#print(UIUC.GetNumOfProfessors(1112))
#UIUC.PrintProfessorInfo()
#UIUC.PrintProfessorDetail()


# Step 1 Input Data into Database or CSV
# Step 2 Refer to github article relating tables to forms so I can see what the user clicked and do the proper query
# Step 3 Use Notepad++ to see what exactly I wanna display