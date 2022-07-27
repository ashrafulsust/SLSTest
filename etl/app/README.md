# Database & Python ETL
This is a simple python ETL application that provision cassandra database and load data into it.

## Workflow

### 1. Build, create and start all the container 

```shell
docker-compose up
```

### 2. Execute python importer script to load data into cassandra 

```shell
docker exec -it etl-app python3 importer.py
```

### 3. Execute python query script to query loaded data

```shell
docker exec -it etl-app python3 query.py
```
