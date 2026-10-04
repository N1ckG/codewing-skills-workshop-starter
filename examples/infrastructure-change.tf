# Fictional exercise. Review only. Do not apply.
# A storage-account change with deliberately unanswered operational questions.
resource "azurerm_storage_account" "demo" {
  name                     = "workshopdemostorage"
  resource_group_name      = "rg-workshop-demo"
  location                 = "westeurope"
  account_tier             = "Standard"
  account_replication_type = "LRS"
  min_tls_version          = "TLS1_2"
  public_network_access_enabled = true

  tags = {
    environment = "demo"
  }
}
