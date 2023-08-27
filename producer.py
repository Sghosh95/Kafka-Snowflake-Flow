from time import sleep
from json import dumps
from kafka import KafkaProducer

topic_name="topic"
producer=KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda a:dumps(a).encode('utf-8'))

for i in range(1000):
    #should be json serializable
    data= {"message :" :i}
    print(data)
    producer.send(topic_name,value=data)
    sleep(2)