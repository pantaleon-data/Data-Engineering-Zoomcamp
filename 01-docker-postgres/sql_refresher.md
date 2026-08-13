Joining Yellow Taxi table with Zones Lookup table (implicit INNER JOIN):
```sql
SELECT
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    total_amount,
    CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
    CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc"
FROM
    yellow_taxi_trips_2021_1 t,
    zones zpu,
    zones zdo
WHERE
    t."PULocationID" = zpu."LocationID"
    AND t."DOLocationID" = zdo."LocationID"
LIMIT 100;
```

Joins taxi trip data with the zones table to find the top 10 pickup locations by trip count.
```sql
SELECT
	CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
	COUNT(*) AS trip_count
FROM
	yellow_taxi_trips_2021_1 t,
	zones zpu
WHERE
	t."PULocationID" = zpu."LocationID"
GROUP BY pickup_loc
ORDER BY COUNT(*) DESC
LIMIT 10;
```
Joins taxi trip data with the zones table twice to identify the top 10 pickup-to-drop-off routes by trip count.
```sql
SELECT
	CONCAT(zpu."Borough", ' | ', zpu."Zone") AS "pickup_loc",
	CONCAT(zdo."Borough", ' | ', zdo."Zone") AS "dropoff_loc",
	COUNT(*) AS trip_count
FROM
	yellow_taxi_trips_2021_1 t,
	zones zpu,
	zones zdo
WHERE
	t."PULocationID" = zpu."LocationID"
	AND t."DOLocationID" = zdo."LocationID"
GROUP BY 
	pickup_loc,
	dropoff_loc
ORDER BY COUNT(*) DESC
LIMIT 10;
```

calculating trip count and average trip distance by drop-off borough.
```sql
SELECT
    zdo."Borough",
    COUNT(*) AS trip_count,
    AVG(t."trip_distance") AS avg_trip_distance
FROM yellow_taxi_trips_2021_1 AS t
JOIN zones AS zdo
    ON t."DOLocationID" = zdo."LocationID"
GROUP BY zdo."Borough"
HAVING COUNT(*) >= 100
ORDER BY avg_trip_distance DESC;
```