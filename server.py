import pika

from config import CONFIG

RABBIT_MQ_SERVER = "localhost"

#print(CONFIG)
#if 'RABBIT_USER' not in CONFIG or 'RABBIT_PASSWORD' not in CONFIG:
 #   raise ValueError('RABBIT_USER or RABBIT_PASSWORD sont manquant dans le fichier .env')
                     
                     
# establish connection with rabbit mq
credentials = pika.PlainCredentials(CONFIG['RABBIT_USER'], CONFIG['RABBIT_PASSWORD'])
parameters = pika.ConnectionParameters(RABBIT_MQ_SERVER, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

