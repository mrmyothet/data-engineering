```sql
SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."borough", ' / ', zpu."zone") AS "pickup_location",
       Concat(zdo."borough", ' / ', zdo."zone") AS "pickup_location"
FROM   green_tripdata t,
       zones zpu,
       zones zdo
WHERE  t."pulocationid" = zpu."locationid"
       AND t."dolocationid" = zdo."locationid"
LIMIT  100;

```

```sql
SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."borough", ' / ', zpu."zone") AS "pickup_location",
       Concat(zdo."borough", ' / ', zdo."zone") AS "pickup_location"
FROM   green_tripdata t
       JOIN zones zpu
         ON t."pulocationid" = zpu."locationid"
       JOIN zones zdo
         ON t."dolocationid" = zdo."locationid"
LIMIT  100;
```

```sql
DELETE FROM zones
WHERE  "locationid" = 95

SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."borough", ' / ', zpu."zone") AS "pickup_location",
       Concat(zdo."borough", ' / ', zdo."zone") AS "pickup_location",
       zpu."locationid",
       zdo."locationid"
FROM   green_tripdata t
       LEFT JOIN zones zpu
              ON t."pulocationid" = zpu."locationid"
       LEFT JOIN zones zdo
              ON t."dolocationid" = zdo."locationid"
LIMIT  100;

SELECT lpep_pickup_datetime,
       lpep_dropoff_datetime,
       total_amount,
       Concat(zpu."borough", ' / ', zpu."zone") AS "pickup_location",
       Concat(zdo."borough", ' / ', zdo."zone") AS "pickup_location",
       zpu."locationid",
       zdo."locationid"
FROM   green_tripdata t
       RIGHT JOIN zones zpu
               ON t."pulocationid" = zpu."locationid"
       RIGHT JOIN zones zdo
               ON t."dolocationid" = zdo."locationid"
LIMIT  100;
```
