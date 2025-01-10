import json
import logging
import os
import uuid
import boto3
from datetime import datetime


# initialize logger
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# replace with your database credentials
DB_ENDPOINT = "your_postgres_endpoint"
DB_USER = "your_postgres_user"
DB_PASSWORD = "your_postgres_password"
DB_NAME = "your_postgres_database"


'''processes events from PostgreSQL and logs them'''
def lambda_handler(event, context):

    try:
        event_data = json.loads(event['Records'][0]['Sns']['Message']) #parses the event

        '''extracts important data from the event,
           change it to match your log structure'''
        
        log_message = event_data.get('message')
        table_name = event_data.get('table_name', 'Unknown')
        query = event_data.get('query', 'No Query')


        '''verification of existence'''
        if log_message is Nonte:
            logging.warning("here is no error message in the event")

            return {'statusCode': 500,
                    'body': json.dumps('Error: Message not found in event.')}

        logging.info(f"event handling: {log_message}")


        '''Connecting to the PostgreSQL database,
           replace with your database credentials'''
        
        conn = psycopg2.connect(host=DB_ENDPOINT, database=DB_NAME,
                                user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()


        '''request for additional actions''' 
        try:
            cur.execute("INSERT INTO your_log_table (log_message, table_name, query, log_time) VALUES (%s, %s, %s, %s)",
                        (log_message, table_name, query, datetime.now()))
            conn.commit()

            logging.info("The PostgreSQL entry was completed successfully")

            return {'statusCode': 200, 'body': json.dumps('Success: Data inserted in PostgreSQL.')}


        except psycopg2.Error as e:
            logging.error(f"Error writing to PostgreSQL: {e}")

            conn.rollback()

            return {'statusCode': 500, 'body': json.dumps(f'Error: {e}')}


        finally:
            cur.close()
            conn.close()


    except (json.JSONDecodeError, KeyError) as e:
        logging.error(f"Error when processing the event: {e}")

        return {'statusCode': 500, 'body': json.dumps(f'Error: Invalid event format - {e}')}
    

    except Exception as e:
        logging.exception(f"Unexpected error: {e}")

        return {'statusCode': 500, 'body': json.dumps(f'Error: {e}')}