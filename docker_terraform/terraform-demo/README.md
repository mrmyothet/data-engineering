```bash

brew tap hashicorp/tap
brew install hashicorp/tap/terraform

```

```bash
export GOOGLE_CREDENTIALS='/Users/macos/my-creds.json'

echo $GOOGLE_CREDENTIALS
```

---

```bash
# Refresh service-account's auth-token for this session
gcloud auth application-default login
```

```bash
# Initialize state file (.tfstate)
terraform init
```

```bash
# Check changes to new infra plan
terraform plan -var="project=ny-rides-mt"

terraform plan # just works after gcloud login
```

```bash
# Create new infra
terraform apply -var="project=ny-rides-mt"

terraform apply 
```

```bash
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```