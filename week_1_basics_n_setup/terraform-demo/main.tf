terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.17.0"
    }
  }
}

provider "google" {
  credentials = "./keys/my-creds.json"
  project     = "mt-terraform-demo"
  region      = "us-central1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "mt-terraform-demo-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}