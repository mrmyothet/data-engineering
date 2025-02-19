variable "project" {
  description = "Project Id"
  default     = "ny-rides-mt"

}

variable "region" {
  description = "Region of the resources"
  default     = "us-central1"

}

variable "credentials" {
  description = "Path to the service account key file"
  default     = "../.google/credentials/google_credentials.json"

}

variable "bq_dataset_name" {
  description = "BigQuery dataset name"
  default     = "ny_taxi"

}

variable "location" {
  description = "Location of the resources"
  default     = "US"

}

variable "gcs_bucket_name" {
  description = "GCS Bucket Name"
  default     = "ny_taxi_data_mt"

}

variable "gcs_storage_class" {
  description = "Bucket Stograge Class"
  default     = "STANDARD"

}