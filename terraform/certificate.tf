resource "yandex_cm_certificate" "certificate" {
  name    = "www-${replace(var.DOMEN, ".", "-")}"
  domains = ["www.${var.DOMEN}"]

  managed {
    challenge_type = "DNS_CNAME"
  }
}

resource "yandex_dns_recordset" "certificate_dns_recordset" {
  zone_id = yandex_dns_zone.zone.id
  name    = yandex_cm_certificate.certificate.challenges[0].dns_name
  type    = yandex_cm_certificate.certificate.challenges[0].dns_type
  data    = [yandex_cm_certificate.certificate.challenges[0].dns_value]
  ttl     = 60
}
