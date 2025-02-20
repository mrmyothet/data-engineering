### Install Terraform on Ubuntu

```bash 
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

```

- Install HashiCorp GPG key: 

```bash 
wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

```

- Verify the key's fingerprint.

```bash
gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

```

- Add the official HashiCorp repository 

```bash 
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

```

- Download the package information from HashiCorp.

```bash
sudo apt update

```

- Install Terraform from the new repository.

```bash
sudo apt-get install terraform

```