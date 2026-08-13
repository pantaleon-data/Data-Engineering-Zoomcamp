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

Showing locations with the highest pickups
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