# Automated DataBase Monitoring

In this project, I have developed an automated system for monitoring and collecting information for the PostgreSQL database. This system collects information from the PostgreSQL database using a python script, stores metrics using Elasticsearch, automates Jenkinsfile activation with a python script thanks to Jenkins, stores logs thanks to Cassandra, and reacts to changes in the PostgreSQL database using the AWS Lambda function and sets up triggers for calling the function.


# Purpose

The purpose of this system is 

- Monitoring the performance of the PostgreSQL database.
- Collecting statistics on key metrics such as CPU usage, query execution time, and database availability.
- Notifying the team about critical events and exceeding thresholds.
- Storing logs of the system for further analysis.


# Content

- [Technologies](#Technologies)
- [Instruction](#Instruction)
- [The project team](#The_project_team)

# Technologies

- [PostgreSQL](#PostgreSQL)
- [Python_3.13.1](#Python_3.13.1)
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

This will show the path to the data files, including « postgresql.conf »

Open the file in the vim text editor

Example: 
vim /usr/local/var/postgres/postgresql.conf
   
Find the shared_preload_libraries line and add pg_stat_statements

shared_preload_libraries = 'pg_stat_statements’ 
   
Save the file

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


# Python_3.13.1


# The project team

- Matsvei Asipenka — DevOps engineer   https://github.com/mt-67/Automated_DB_Monitoring.git

