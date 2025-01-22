variable "project" {
  description = "Project Id"
  default     = "mt-terraform-demo"

}

variable "region" {
  description = "Region of the resources"
  default     = "us-central1"

}

variable "credentials" {
  description = "Path to the service account key file"
  default     = "./keys/my-creds.json"

}

variable "bq_dataset_name" {
  description = "BigQuery dataset name"
  default     = "demo_dataset"

}

variable "location" {
  description = "Location of the resources"
  default     = "US"

}

variable "gcs_bucket_name" {
  description = "GCS Bucket Name"
  default     = "mt-terraform-demo-terra-bucket"

}

variable "gcs_storage_class" {
  description = "Bucket Stograge Class"
  default     = "STANDARD"

}