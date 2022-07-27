#!/usr/local/bin/python3
import os
import csv
from cassandra.cluster import Cluster

KEYSPACE = os.environ["CASSANDRA_KEYSPACE"]
cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS test WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
""")

cluster = Cluster([os.environ["CASSANDRA_IP_ADDRESS"]], port=9042)
session = cluster.connect(KEYSPACE, wait_for_all_pools=True)

session.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id int,
        first_name text,
        last_name text,
        email text,
        gender text,
        ip_address text,
        PRIMARY KEY (id)
    )
""")

query = session.prepare("""
    INSERT INTO data (id, first_name, last_name, email, gender, ip_address) VALUES (?, ?, ?, ?, ?, ?)
""")

with open("data.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(f"Inserting row {row}")
        session.execute(query, (int(row['id']), row['first_name'], row['last_name'], row['email'], row['gender'], row['ip_address']))

    print("Successfully Completed")
