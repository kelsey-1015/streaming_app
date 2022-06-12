# run the command to start all services in the correct order -d run in detach mode
docker-compose up -d
# check running containers
docker container ls
# create a topic
docker exec broker \
kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic demo


# write messages to the topic quickstart, use the kafka-console-producer command line tool. This is normally used for trouble shooting. Use Producer API or Kafka Connect for pulling data from other systems.

docker exec -it broker \
kafka-console-producer --bootstrap-server broker:9092 \
                       --topic demo


# open a new terminal and run the command to launch the kafka-console-consumer --from-beginning argument means the messages will be read from the start of the topic, in practice you’ll use the Consumer API in your application code, or Kafka Connect for reading data from Kafka to push to other systems.

docker exec --it broker \
kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic demo \
                       --from-beginning

# Press Ctrl-D to exit the producer, and Ctrl-C to stop the consumer.

# Access webUI with local brower 
localhost:8080

# Acheive the url for spark master and execute into spark master container

docker exec -it container_name bash

# for spark node, the master node addresses changes over time
./bin/spark-submit --master spark://ee53ec93387b:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 app_code/spark_kafka_streaming.py

./bin/spark-submit --class Streaming --master spark://ee53ec93387b:7077 --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.1 app_code/spark_kafka_streaming_1.py 

# stop the kafka broker
docker-compose down


