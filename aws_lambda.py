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

        '''extracts important data from the event
           change it to match your log structure'''
        
        log_message = event_data.get('message')
        table_name = event_data.get('table_name', 'Unknown')
        query = event_data.get('query', 'No Query')


        '''verification of existence'''
        if log_message is None:
            logging.warning("there is no error message in the event")
            
            return {'statusCode': 500,
                    'body': json.dumps('Error: Message not found in event.')}

        logging.info(f"event handling: {log_message}")


        '''Connecting to the PostgreSQL database,
           replace with your database credentials'''
        conn = psycopg2.connect(host=DB_ENDPOINT, database=DB_NAME,
                                user=DB_USER, password=DB_PASSWORD)
        cur = conn.cursor()