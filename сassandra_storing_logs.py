import logging
import uuid
import time
from cassandra.cluster import Cluster 
from cassandra.auth import PlainTextAuthProvider 


# configuring logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


'''writes the error to the table Cassandra'''
def log_error_to_cassandra(message, table_name, query, error_code, duration):
    try:
        # connecting to a Cassandra cluster, replace it with your data
        cloud_config = {'secure_connect_bundle': 'secure-connect.zip'}

        auth_provider = PlainTextAuthProvider(username='your_cassandra_username',
                                              password='your_cassandra_password')
        
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect('monitoring')

        log_id = str(uuid.uuid4())
        now = time.time()
        try:
            session.execute(
                """
                INSERT INTO monitoring.logs (id, message, timestamp, table_name, query, error_code, duration)
                VALUES (%(id)s, %(message)s, %(timestamp)s, %(table_name)s, %(query)s, %(error_code)s, %(duration)s)
                """,
                {
                 'id': log_id,
                 'message': message,
                 'timestamp': now,
                 'table_name': table_name,
                 'query': query,
                 'error_code': error_code,
                 'duration': duration
                }
            )
            logging.info(f"The data is recorded in Cassandra: log_id={log_id}")

        except Exception as e:
            logging.error(f"Error: {e}")


        session.shutdown()
        cluster.shutdown()

    except Exception as e:
        logging.error(f"Error connecting to Cassandra: {e}")


if __name__ == "__main__":
    try:
        log_error_to_cassandra(message="Error when making a request to users",
                               table_name="users",
                               query="SELECT FROM users",
                               error_code=100,
                               duration=150)
    except Exception as e:
        logging.error(f"Error when executing the script: {e}")