import psycopg2 # connecting to the database
import psutil  # CPU usage
import time
import requests  # sending data to elasticsearch


'''RAM usage by the database'''
def memory_usage():  

    conn = psycopg2.connect(dbname="Aero", user="user_name",
                            password="password", host="localhost")
    cursor = conn.cursor()
    cursor.execute("SELECT pg_total_relation_size(company, pass_in_trip, passenger, trip);")  
    
    memory_use = cursor.fetchone()[0]
    conn.close()
    return memory_use


'''CPU load'''
def cpu_usage():

    return psutil.cpu_percent(interval=1)