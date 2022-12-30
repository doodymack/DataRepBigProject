"# BigProject"  

# H Dip in Data Analytics 2021-2022
# Data Representation
## Winter Semester Assessment
***
<br>
by Paul Mc Grath


## Introduction

In approaching this project the aim was to build on the course material and demonstrate API/FLASK/CRUD/DAO/Server functionality knowledge <br> 
and to how these can be combined to create something useful. <br>
NB: The decision to use a 'Rick & Morty' theme was NOT based on any bias of potential tutor interest! <br>
In looking for a topic I was guided by creating something that my teenage son who is a R&M fan would connect with <br>

The aim was to modify the apps put forward in the course to be an online episode voting machine for R&M <br>
Footnote: My son when presented with the app asked 'why only season 1'! <br>

## Requirements

Python 3.17 or more recent installed in your machine
MS Edge or Google Chrome
MySQL Server (WampServer or Equivalent)
CMD or VS Code 

## How to Run 

There are two 'webpages' 1. randm which is hosted  2. RAM-CRUD which is run locally <br><br>

## randm on PythonAnywhere

### Option 1:

A website was created on the style of the voting app presented in the course. <br>
The website returns a list of Rick&Morty season 1 episodes along with titles. <br>
There is a hyperlink to a synopses page (fandom) for a reminder of each episode synopses. <br>
The votes are tallied in the MySQL server setup in pythonanywhere account and pushef to the results page. <br>

https://doodymack.pythonanywhere.com/vote.html

https://doodymack.pythonanywhere.com/results.html

### Offline Option:

1. Execute server by running 'python server1.py' in randm folder on command line
2. Paste in the local server address (i.e. http://127.0.0.1:5000/) to web and add:
3. This '/.html' or '/index.html' wil return a test output 
4. http://127.0.0.1:5000/vote.html will return the vote page for Series 1
5. http://127.0.0.1:5000/results.html  will return the updated tally from the local server

![image](https://user-images.githubusercontent.com/77808597/210068890-93a8b99b-1d71-4af5-b8ab-f31f098b48f0.png)
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| datarep            |
| datarepresentation |
| mysql              |
| performance_schema |
| project            |
| sys                |
| test               |
+--------------------+
8 rows in set (0.00 sec)

mysql> use project;
Database changed
mysql> show tables;
+-------------------+
| Tables_in_project |
+-------------------+
| episodevote       |
| vote              |
+-------------------+
2 rows in set (0.00 sec)

mysql> select * from episodevote;
+----+---------------------------------------------+-----------+
| id | episode                                     | ipaddress |
+----+---------------------------------------------+-----------+
|  1 | S1E1: PILOT                                 | 127.0.0.1 |
|  2 | S1E2: Lawnmower Dog                         | 127.0.0.1 |
|  3 | S1E1: PILOT                                 | 127.0.0.1 |
|  4 | S1E3: Anatomy Park                          | 127.0.0.1 |
|  5 | S1E4: M. Night Shaym-Aliens                 | 127.0.0.1 |
|  6 | S1E10: Close Rick-counters of the Rick Kind | 127.0.0.1 |
|  7 | S1E8: Rixty Business                        | 127.0.0.1 |
|  8 | S1E1: PILOT                                 | 127.0.0.1 |
+----+---------------------------------------------+-----------+
8 rows in set (0.00 sec)

mysql>

As the pythonanywhere hosted 'voting' app did not utilise all the CRUD funvtionality demonstrated in the courseshow databases, I created another webpage<br>
that runs on LOCAL server.  This was based on bookviewer structure.  This allows the user to<br>
manually enter a series name (number), episode name (number) and give it a rating. <br>
This could be modified before being hosted to allow people input their vote for their favourite episode. <br>



## RAM: CRUD:

1. Execute server by running 'python server1.py' in RAM CRUD folder on command line
2. Paste in the local server address (i.e. http://127.0.0.1:5000/) to web and add:
3. This '/.html' or '/index.html' wil return a test output 
4. http://127.0.0.1:5000/randmviewer.html will return the ranking page with CRUD functionality
5. http://127.0.0.1:5000/results.html  will return the updated tally from local server (see below)



mysql> use datarepresentation;
Database changed
mysql> show tables;
+------------------------------+
| Tables_in_datarepresentation |
+------------------------------+
| book                         |
| rickandmorty                 |
| student                      |
+------------------------------+
3 rows in set (0.00 sec)

mysql> select * from rickandmorty;
+----+--------+---------+--------+
| id | series | episode | rating |
+----+--------+---------+--------+
|  1 | 4      | 2       |      3 |
|  2 | 5      | 3       |      5 |
+----+--------+---------+--------+
2 rows in set (0.02 sec)

Test 'CREATE' button on webpage:

mysql> select * from rickandmorty;
+----+--------+---------+--------+
| id | series | episode | rating |
+----+--------+---------+--------+
|  1 | 4      | 2       |      3 |
|  2 | 5      | 3       |      5 |
|  3 | 4      | 2       |      3 |
+----+--------+---------+--------+
3 rows in set (0.00 sec)

mysql>



#### Future work

RAM CRUD Flask server runs on LOCAL server only. The RAM-CRUD could be modified before being hosted to allow people input their vote for their favourite episode.<br> 


### Conclusion:

The project allowed me to improve my working knowledge of API Servers, how to download data, modify and output. <br> 
Using the skills I picked up on the module I was able to create two different Flask Servers to display interactive <br>
webpages that have functionality.  These allow user input at the front end, that can be processed by the FLASK server, <br>
which in turn links to a DAO to process the input and putput to a database (MySQL). <br>
Once hosted online it allows for user inputs be taken in and stored and as required outputted to a separate webpage.<br>


## Contact: 

[doodymack@gmail.com](mailto:doodymack@gmail.com)


references:

https://github.com/andrewbeattycourseware/datarepresentation
