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


'''query execution time'''
def execution_time():
    
    conn = psycopg2.connect(dbname="Aero", user="user_name",
                            password="password", host="localhost")
    cursor = conn.cursor()

    start_time = time.time()

    cursor.execute("SELECT * FROM company, pass_in_trip, passenger, trip;") # or any of your other requests 
    cursor.fetchall()

    end_time = time.time()
    
    conn.close()
    return end_time - start_time


'''database availability'''
def check_availab():
    try:
        conn = psycopg2.connect(dbname="Aero", user="user_name",
                                password="password", host="localhost")
        conn.close()
        return True
    
    except psycopg2.OperationalError:
        return False
    

'''collecting all metrics'''
def all_metrics():

    metrics = {'memory_usage': memory_usage(),
               'cpu_usage': cpu_usage(),
               'query_execution_time': execution_time(),
               'database_available': check_availab()}
    return metrics


'''sending metrics to elasticsearch'''
def send_metrics(metrics):

    url = 'http://localhost:9200/metrics/_doc/'  # replace elasticsearch with your URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=metrics, headers=headers)
    
    if response.status_code == 201:
        print("metrics sent to elasticsearch")
    else:
        print(f"error when sending metrics: {response.status_code}, {response.text}")


if __name__ == "__main__":
    metrics = all_metrics()
    print(metrics) 

    send_metrics(metrics)  # sending metrics to elasticsearch