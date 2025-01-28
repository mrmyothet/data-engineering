```sql
SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       Concat(zdo."Borough", ' / ', zdo."Zone") AS "pickup_location"
FROM   green_tripdata t,
       Zones zpu,
       Zones zdo
WHERE  t."PULocationID" = zpu."LocationID"
       AND t."DOLocationID" = zdo."LocationID"
LIMIT  100;

```

### Using an explict INNER JOIN

```sql
SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       Concat(zdo."Borough", ' / ', zdo."Zone") AS "pickup_location"
FROM   green_tripdata t
       JOIN Zones zpu
         ON t."PULocationID" = zpu."LocationID"
       JOIN Zones zdo
         ON t."DOLocationID" = zdo."LocationID"
LIMIT  100;
```

### Using LEFT, RIGHT, OUTER JOIN when LocationID are not in either tables

```sql
DELETE FROM Zones
WHERE  "LocationID" = 95

SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       Concat(zdo."Borough", ' / ', zdo."Zone") AS "pickup_location",
       zpu."LocationID",
       zdo."LocationID"
FROM   green_tripdata t
       LEFT JOIN Zones zpu
              ON t."PULocationID" = zpu."LocationID"
       LEFT JOIN Zones zdo
              ON t."DOLocationID" = zdo."LocationID"
LIMIT  100;

SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."Borough", ' / ', zpu."Zone") AS "pickup_location",
       Concat(zdo."Borough", ' / ', zdo."Zone") AS "pickup_location",
       zpu."LocationID",
       zdo."LocationID"
FROM   green_tripdata t
       RIGHT JOIN Zones zpu
               ON t."PULocationID" = zpu."LocationID"
       RIGHT JOIN Zones zdo
               ON t."DOLocationID" = zdo."LocationID"
LIMIT  100;
```

### Using GROUP BY to calculate the number of trips per day

```sql
SELECT
  CAST(tpep_dropoff_datetime as DATE) as "day",
  COUNT(1)
FROM
  yellow_tripdata t
GROUP BY
  CAST(tpep_dropoff_datetime as DATE);
```

### Using ORDER BY to find most busy day

```sql
SELECT
  CAST(tpep_dropoff_datetime as DATE) as "day",
  COUNT(1) as "count"
FROM
  yellow_tripdata t
GROUP BY
  CAST(tpep_dropoff_datetime as DATE)
ORDER BY "count" DESC;
```

### Other kinds of Aggregations

```sql
SELECT
  CAST(tpep_dropoff_datetime as DATE) as "day",
  COUNT(1) as "count",
  MAX(total_amount) as max_total_amount,
  MAX(passenger_count) as max_passenger_count
FROM
  yellow_tripdata t
GROUP BY
  CAST(tpep_dropoff_datetime as DATE)
ORDER BY "max_total_amount" DESC;
```

### Grouping by multiple fields

```sql
SELECT
  CAST(tpep_dropoff_datetime as DATE) as "day",
  "DOLocationID",
  COUNT(1) as "count",
  MAX(total_amount) as max_total_amount,
  MAX(passenger_count) as max_passenger_count
FROM
  yellow_tripdata t
GROUP BY
  1, 2
ORDER BY
"day" ASC,
"DOLocationID" ASC;
```
