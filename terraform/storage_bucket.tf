resource "yandex_iam_service_account_static_access_key" "sa-static-key" {
    service_account_id = var.SERVICE_ACCOUNT_ID
    description        = "static access key for object storage"
}

resource "yandex_storage_bucket" "storage" {
    access_key = yandex_iam_service_account_static_access_key.sa-static-key.access_key
    secret_key = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
    bucket = "www.${var.DOMEN}"
    acl    = "public-read"

    website {
        index_document = "index.html"
        error_document = "index.html"
    }

    https {
        certificate_id = yandex_cm_certificate.certificate.id
    }
}

resource "yandex_dns_recordset" "storage_dns_recordset" {
  zone_id = yandex_dns_zone.zone.id
  name    = "www.${var.DOMEN}."
  type    = "ANAME"
  ttl     = 200
  data    = [yandex_storage_bucket.storage.website_endpoint]
}
