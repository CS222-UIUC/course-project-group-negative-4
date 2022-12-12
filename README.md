Bryan Finn, Dherya Jalan, Jaywoo Jo

## UIUC Courses and Instructor Data Website

### Functionality
UIUC Course Data is an all in one place to help students make informed decisions
regarding course selection. For a given course, we provide specific statistical course data for past semester
grade distributions and links to RateMyProfessor reviews and Reddit posts.

1. Users can look up a course code (e.g. CS 225) to view what professors have
taught the class in the past.
2. For the searched course, users will have access to a data visualization spread (the number of A+’s/A’s/A-’s, etc.) for all different sections taught in recent history, RateMyProfessor links for the professors who teach the course, and links to Reddit posts about the course.

<table>
  <tr>
    <td> Home Page</td>
     <td> Ex. search, STAT 400 p.1 </td>
     <td> Ex. search, STAT 400 p.2</td>
  </tr>
  <tr>
    <td valign="top"><img src="https://github.com/CS222-UIUC/course-project-group-negative-4/blob/main/README-Images/1.png"></td>
    <td valign="top"><img src="https://github.com/CS222-UIUC/course-project-group-negative-4/blob/main/README-Images/2.png"></td>
    <td valign="top"><img src="https://github.com/CS222-UIUC/course-project-group-negative-4/blob/main/README-Images/3.png"></td>
  </tr>
 </table>

### Technical Architecture
insert explanation

![Technical Architecture Image](https://github.com/CS222-UIUC/course-project-group-negative-4/blob/main/README-Images/CS222-Framework.jpeg)

### Development
Best to create a [python virtual environment](https://phoenixnap.com/kb/install-flask#ftoc-heading-6). 
Activate the environment by running ```<name of environment>/bin/activate```. If issues arise, write ```source <name of environment>/bin/activate```.

After activating virtual env, to install dependencies, run ```pip install -r requirements.txt```.

Open the file 'main.py' on your IDE (i.e. VS Code) and press run. Flask should then provide you with a link to run the application, such as "http://127.0.0.1:5000", which you can open in your browser.

### Group Members and Roles
**Bryan Finn:** Frontend and initial application template design (HTML/CSS/Bootstrap/Flask); RMP & Reddit backend integration (Flask).  
**Dherya Jalan:** Backend integration for GPA visualization (Flask); Visualization creation (Matplotlib).  
**Jaywoo Jo:** Frontend and UI/UX design (HTML/CSS); Data manipulation using GPA & RMP CSV files (Pandas); Visualization creation and image adjustment for website integration (Matplotlib).  
