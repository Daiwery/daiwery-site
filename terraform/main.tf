terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

# From env
variable "TOKEN" { type = string }
variable "CLOUD_ID" { type = string }
variable "FOLDER_ID" { type = string }
variable "ZONE" { type = string }
variable "SERVICE_ACCOUNT_ID" { type = string }
variable "DOMEN" { type = string }

provider "yandex" { 
  token     = var.TOKEN
  cloud_id  = var.CLOUD_ID
  folder_id = var.FOLDER_ID
  zone      = var.ZONE
}

output "access_key" {
  value = yandex_iam_service_account_static_access_key.sa-static-key.access_key
}

output "secret_key" {
  value = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
  sensitive = true
}

