for ingesting zones ingest_data
```python
docker run -it --rm \
  --network=01-docker-postgres_default \
  taxi_ingest:v001 \
  python ingest_data2.py \
  --target-table=zones \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi
```

for ingesting taxi trips data
```python
docker run -it --rm \
  --network=01-docker-postgres_default \
  taxi_ingest:v001 \
  python ingest_data.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=pgdatabase \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=yellow_taxi_trips_2021_1 \
  --year=2021 \
  --month=1 \
  --chunksize=100000
  ```