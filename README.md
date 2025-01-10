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







```Bash
systemctl status postgresql
```
# The project team

