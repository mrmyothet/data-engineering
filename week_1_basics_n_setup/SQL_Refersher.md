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

```
