# Automated DataBase Monitoring

In this project, I have developed an automated system for monitoring and collecting information for the PostgreSQL database. This system collects information from the PostgreSQL database using a python script, stores metrics using Elasticsearch, automates Jenkinsfile activation with a python script thanks to Jenkins, stores logs thanks to Cassandra, and reacts to changes in the PostgreSQL database using the AWS Lambda function and sets up triggers for calling the function.


# Purpose

The purpose of this system is 

- Monitoring the performance of the PostgreSQL database.
- Collecting statistics on key metrics such as CPU usage, query execution time, and database availability.
- Notifying the team about critical events and exceeding thresholds.
- Storing logs of the system for further analysis.


# Content
- [Automated DataBase Monitoring](#Automated_DataBase_Monitoring)
- [Purpose](#Purpose)
- [Content](#Content)
- [Technologies](#Technologies)
- [Instruction](#Instruction)
- [The project team](#The_project_team)


# Technologies

- [PostgreSQL](#PostgreSQL)
- [Python](#Python)
- [Elasticsearch](#Elasticsearch)
- [Kibana](#Kibana)
- [Jenkins](#Jenkins)
- [Cassandra](#Cassandra)
- [AWS Lambda](#AWS_Lambda)
- [Groovy](#Groovy)
- [Bash](#Bash)
- [Ubuntu](#Ubuntu)


# Instruction

# PostgreSQL

The databases of 5 airlines were used as a basis.
Collecting metrics for monitoring.


Customization 

Install PostgreSQL. Download the database from the file in the « Aero_pg_script.sql » repository. Create an Aero database.

Activate the pg_stat_statements extension to collect statistics.
- RAM memory usage
- CPU usage
- Query execution time
- Database availability


The algorithm of actions for activating this extension :

Find the location of the « postgresql.conf » file, it is located in the PostgreSQL data directory.
   
Type Bash into the console
```Bash
systemctl status postgresql
```

This will show the path to the data files, including « postgresql.conf ».

Open the file in the vim text editor.

Example: 
vim /usr/local/var/postgres/postgresql.conf
   
Find the shared_preload_libraries line and add pg_stat_statements

shared_preload_libraries = 'pg_stat_statements’ 
   
Save the file.

Restart the PostgreSQL server

```Bash
sudo systemctl restart postgresql
```

After restarting the database connection, write the 

```PostgreSQL
CREATE EXTENSION pg_stat_statements command;
```

Check the functionality of the extension using the command

```PostgreSQL
SELECT * FROM pg_stat_statements;
```

Now you can use pg_stat_statements to collect statistics.


# Python

In the script repository « script_for_db_and_elastic.py » python will be able to output the collected statistics from our database and connect elasticsearch to our database.

In the script repository « cassandra_storing_logs.py » python, logs will be recorded in Cassandra.

In the script repository « aws_lambda.py » python will respond to events in PostgreSQL and set up triggers for calling the function.


# Elasticsearch

Let's connect and configure Elasticsearch to graphically display statistics from our database. 

To interact with Elasticsearch through the graphical interface, we will use Kibana, which provides a user-friendly interface for working with data in Elasticsearch. 


Customization

Algorithm of actions :


Run Kibana and Elasticsearch from their files in the console.

After launch, you will be able to access the Kibana interface via at http://localhost:5601 



To create an index in Elastic:


Go to the "Management" section in the side menu.

Select "Index Patterns" 

Click on the "Create index pattern" button. 

Specify the index name (for example, my-index-*) and follow the on-screen instructions.



To make requests:


Go to the "Discover" section to view the data in your index.

You can use filters and search to find the information you need.



To create visualizations:


 Go to the "Visualize" section to create graphs and charts based on your data.

 Select the visualization type, adjust the settings, and save the results.



To create a Dashboard:


 In the Dashboard section, you can assemble visualizations together and create interactive Dashboards for data monitoring.


 # Jenkins

Install and connect Jenkins via the console 

I wrote a groovy script in the « Jenkinsfile » in the repository to activate a Python script that will be automatically triggered in Jenkins in free jobs every 15 minutes.


Customization

Long-range algorithm for automatic operation of Jenkins free jobs :

Create free jobs in Jenkins with the name
automated-db-monitoring

Description
Takes a python script from the GitHub repository

In Source Code Management
include Git
in the Repository URL and write https://github.com/mt-67/Automated_DB_Monitoring.git
in Branches to build, write */main

In Triggers
enable Run periodically
write the code under Schedule  « H/15 * * * * » 

In the Assembly Steps
section, write cat in the Command « script_for_db_and_elastic.py » Create free jobs in Jenkins with the name 
« automated-db-monitoring »


# Cassandra

You need to install Cassandra through a virtual machine on Ubuntu.

Cassandra will store the logs of our database, for this we have written a python script « cassandra_storing_logs.py »


# AWS Lambda

Install the AWS CLI in the console.

I wrote the script « aws_lambda.py » AWS Lambda function in Python for responding to events in PostgreSQL and has set up triggers for calling the function.


# The project team

- Matsvei Asipenka — DevOps engineer  https://github.com/mt-67/Automated_DB_Monitoring.git

