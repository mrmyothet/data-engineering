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
