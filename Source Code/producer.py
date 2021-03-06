# To Create meetUpProducer topic
# ./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic meetUpProducer

# Import Required Libraries
import websocket
import time
from kafka import KafkaProducer

# Sending data to kafka
def on_message(ws, message):
     producer.send('meetUpProducer', message)
     producer.flush()

# Creating Kafka Producer
producer = KafkaProducer(value_serializer=lambda m: str(m).encode("utf-8"),
                         bootstrap_servers=['localhost:9092'])

# Creating Streaming Socket
ws = websocket.WebSocketApp("wss://stream.meetup.com/2/rsvps", on_message=on_message)

# Gets the data continuously
ws.run_forever()
