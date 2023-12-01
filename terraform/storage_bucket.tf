resource "yandex_iam_service_account_static_access_key" "sa-static-key" {
    service_account_id = var.SERVICE_ACCOUNT_ID
    description        = "static access key for object storage"
}

resource "yandex_storage_bucket" "tf-test-bucket" {
    access_key = yandex_iam_service_account_static_access_key.sa-static-key.access_key
    secret_key = yandex_iam_service_account_static_access_key.sa-static-key.secret_key
    bucket = "www.test.daiwery.com"
    acl    = "public-read"

    website {
        index_document = "index.html"
        error_document = "error.html"
    }
}