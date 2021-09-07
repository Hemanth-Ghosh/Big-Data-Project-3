# Big-Data-Project-3
Real-Time Meetup RSPV Data Processing using Kafka and Spark
###### By: Hemanth Ghosh

## Project Description

Spark Streaming of RSVPs from meetup.com API using Kafka meetup.com provides a streaming data of RSVPs in JSON Format.

We utilized Apache Kafka for building real-time pipelines and Apache Spark to do real-time analysis and matplotlib for visualization. As and when an RSVP response is made by a user, our Kafka Producer receives that message through meetup’s web socket and feeds it to a topic. Then Kafka’s Consumer which has subscribed to that topic sends it to Spark’s streaming platform where only the U.S. messages are filtered and real time analysis to get the trending cities within the U.S. takes place. Then the results of the analysis get stored to a text file in our local system, using which visualizations is done in near real time using matplotlib.

This project can be extended to get the real time trending topics across the world or for a specific geography along with other business insights. By giving real time trends in topics like in twitter, users of meetup will be aware of the more popular and less popular topics in near real time. With minor modifications, this project can also be extended to process and analyze IoT data.

## Technologies Used

* **Apache Kafka [2.8]**
Apache Kafka is a framework implementation of a software bus using stream-processing.The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds.

* **Apache Spark [3.1.2]** 
Apache Spark is an open source unified analytics engine for large scale data
processing Spark provides an interface for programming entire clusters with implicit data parallelism
and fault tolerance.

* **Hadoop Hdfs**
HDFS is a distributed file system that handles large data sets running on commodity hardware. It is used to scale a single Apache Hadoop cluster to hundreds (and even thousands) of nodes. 

* **AWS S3**
Amazon S3 or Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its global e-commerce network.

* **Python [3.8]** 
Python is an interpreted high level general purpose programming language
Python's design philosophy emphasizes code readability with its notable use of significant
indentation.

* **PySpark [3.1.2]** 
PySpark is an interface for Apache Spark in Python It not only allows you to
write Spark applications using Python APIs, but also provides the PySpark shell for interactively
analyzing your data in a distributed environment.

* **Git /GitHub** 
It is a provider of Internet hosting for software development and version control
using Git It offers the distributed version control and source code management functionality of Git.

## Features (Problem Statements)

1. What are the current active cities in India which are scheduling Meetup Events?
2. What are the trending topics in US Meetup Events?
3. How many Big data Meetup Events events scheduled in Mumbai?

**TODOs for future development**

This project can be extended to get the real time trending topics across the world or for a specific geography along with other business insights. By giving real time trends in topics like in twitter, users of meetup will be aware of the more popular and less popular topics in near real time. With minor modifications, this project can also be extended to process and analyze IoT data.

## Getting Started

Assuming Kafka and Spark of appropriate version is installed, the following commands are used to run the application.

Spark Streaming integeration with kafka 0.10.0.0 and above, is still in experimental status, Hence using Kafka 0.9 (http://spark.apache.org/docs/latest/streaming-kafka-integration.html)

Run Zookeeper to maintain Kafka, command to be run from Kafka root dir

      bin/zookeeper-server-start.sh config/zookeeper.properties
   
Start Kafka server, aditional servers can be added as per requirement.

      bin/kafka-server-start.sh config/server.properties
   
Start Producer.py to start reading data from the meetup stream and store it in '''meetup''' kafka topic.

Start Consumer.py to consume the stream from the '''meetup''' topic

Submit the spark job spark_meetup.py, to read the data into Spark Streaming from Kafka.

Spark depends on a external package for kafka integeration

      bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.1 spark_meetup.py localhost:2181 meetup

An analysis of number of RSVPs from various cities in "US" region is performed on the RSVPs Stream.


## Dataset Used

 The stream is accesible through: 
 [Meetup.com](http://stream.meetup.com/2/rsvps)
## License
This project uses the following license:
[MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)
