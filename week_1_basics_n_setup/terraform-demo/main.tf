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
  project     = "terraform-demo"
  region      = "us-central1"
}