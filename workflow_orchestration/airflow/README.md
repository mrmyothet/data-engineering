```bash

docker-compose build

docker-compose up airflow-init

docker-compose up

```

### Optional Lightweight local setup for airflow

- Remove redis, worker, triggerer and flower
- Remove depends on redis
- Change Core Executor from CeleryExecutor to LocalExecutor

```bash
docker-compose down --volumes --rmi all
```
