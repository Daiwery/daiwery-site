resource "yandex_dns_zone" "zone" {
  name   = "${replace(var.DOMEN, ".", "-")}-zone"
  zone   = "${var.DOMEN}."
  public = true
}