### Configure SSH

```bash
ssh-keygen -t rsa -f gcp -C myothet -b 2048
```

```bash
ssh -i ~/.ssh/gcp myothet@<External IP Address>

gcloud --version

wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh

bash Anaconda3-2024.10-1-Linux-x86_64.sh

less .bashrc

which python

source .bashrc
```

### Install Docker

```bash

sudo apt-get update
sudo apt-get install docker.io

```

- Install VS Code Extension - Remote SSH
- Run Docker commands without sudo
- https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md

```bash
sudo groupadd docker
sudo gpasswd -a $USER docker
sudo service docker restart
Ctrl D - logout
ssh de-zoomcamp-mt

docker run hello-world
docker run -it ubuntu bash

```

- clone the repo with https option

```bash
git clone https://github.com/DataTalksClub/data-engineering-zoomcamp.git
```

### Install Docker-Compose

```bash

mkdir bin
cd bin
wget https://github.com/docker/compose/releases/download/v2.32.4/docker-compose-linux-x86_64 -O docker-compose
chmod +x docker-compose
./docker-compose --version

nano .bashrc
export PATH="${HOME}/bin:${PATH}"

source .bashrc
which docker-compose

docker-compose --version

```
