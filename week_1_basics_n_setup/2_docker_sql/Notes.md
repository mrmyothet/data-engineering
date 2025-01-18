### Running Docker

```bash
docker run hello-world

docker run -it ubuntu bash

docker run -it python:3.9
```

```bash

docker run -it --entrypoint=bash python:3.9
pip install pandas
python
import pandas
pandas.__version__

```

### Build Dockerfile

```bash

docker build -t test:pandas .
docker run -it test:pandas

docker run -it test:pandas 2025-01-18

```
