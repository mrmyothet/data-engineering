### What is an Orchestrator?

An orchestrator is a tool or system that manages the coordination and execution of complex workflows, tasks, or processes across distributed systems.  
It ensures that the individual tasks in a workflow are executed in the right order, at the right time, and under the right conditions.

Orchestrators are commonly used in domains like:

- Data engineering (ETL/ELT pipelines)
- Microservices (service communication and automation)
- Container management (Kubernetes for orchestrating containers)
- Workflow automation (task scheduling and dependency management)

### Kestra

Kestra is an open-source, event-driven orchestration platform that makes both scheduled and event-driven workflows easy.  
By bringing Infrastructure as Code best practices to data, process, and microservice orchestration, you can build reliable workflows directly from the UI in just a few lines of YAML.

### Install Kestra with docker

```bash
docker run \
--pull=always \
--rm -it \
-p 8080:8080 \
--user=root \
-v /var/run/docker.sock:/var/run/docker.sock \
-v /tmp:/tmp \
kestra/kestra:latest server local
```

```bash
git config --global alias.st status

git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

git config --global alias.cm "commit -m"
```
