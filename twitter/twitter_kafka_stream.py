import os
import tweepy
from dotenv import load_dotenv
from os.path import join, dirname
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092') 

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
topic_name = "demo"

bearer_token = os.environ["BEARER_TOKEN"]

class MyStreamer(tweepy.StreamingClient):
    def on_data(self, raw_data):
        producer.send(topic_name, raw_data)
        print(raw_data)

streamer = MyStreamer(bearer_token)
streamer.add_rules(tweepy.StreamRule("ukraine lang:en"))

# to connect and run a stream 
streamer.filter()
