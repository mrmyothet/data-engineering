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
