import logging
import os
import json
from dotenv import load_dotenv, find_dotenv
import requests
from itertools import islice
from kafka import KafkaProducer

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load .env file
load_dotenv(find_dotenv())
    
kafka_config = {
    'bootstrap.servers': '20.253.120.190:31092',  # Your broker address and port
    'security.protocol': 'SSL',
    'ssl.ca.location': 'C:\Source\ortege\etl\ca.cert',  # Replace with the exact path in your machine
}

# Access environment variable
base_url = os.getenv('BASE_URL')

def get_blocks_in_batch(start_block, end_block, batch_size=100):
    """
    Fetch blocks in batches from start_block to end_block.
    """
    for block_num in range(start_block, end_block, batch_size):
        batch_end = min(block_num + batch_size, end_block)
        batch_urls = [base_url + "/blocks/by_height/" + str(num) for num in range(block_num, batch_end)]
        responses = [requests.get(url) for url in batch_urls]

        for response in responses:
            if response.status_code == 200:
                logging.info(f"Successfully fetched block at {response.url}")
                yield response.json()
            else:
                logging.error(f"Failed to fetch block at {response.url} - Status Code: {response.status_code}")


def push_to_redpanda(data, topic):
    """
    Push data to a RedPanda topic.
    """
    try:
        # Corrected to use KafkaProducer
        producer = KafkaProducer(bootstrap_servers=kafka_config['bootstrap.servers'],
                                 security_protocol=kafka_config['security.protocol'],
                                 ssl_cafile=kafka_config['ssl.ca.location'])
        producer.send(topic, value=data.encode('utf-8'))
        producer.flush()
        logging.info(f"Successfully pushed data to RedPanda topic: {topic}")
    except Exception as e:
        logging.error(f"Error pushing data to RedPanda: {e}")



def get_latest_block_number():
    response = requests.get(base_url)  # Assuming this endpoint gives the latest block number
    if response.status_code == 200:
        data = response.json()
        block_height = data.get('block_height')
        if block_height is not None:
            print("Block Height:", block_height)
            return block_height
        else:
            print("Block height not found in response.")
    else:
        print("Error fetching latest block number:", response.status_code, response.reason)
    return None

# Example usage
#latest_block_number = get_latest_block_number()
latest_block_number = 10

if latest_block_number:
    logging.info(f"Latest block number is {latest_block_number}. Starting to fetch blocks...")
    for block_data in get_blocks_in_batch(0, int(latest_block_number) + 1):
        # Assuming block_data is serializable to JSON
        push_to_redpanda(json.dumps(block_data), "etl_dev_br_aptos_blocks")

