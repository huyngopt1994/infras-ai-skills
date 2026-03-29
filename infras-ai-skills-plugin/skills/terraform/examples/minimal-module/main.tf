locals {
  common_tags = {
    environment = var.environment
    managed_by  = "terraform"
    project     = var.project_name
    owner       = var.owner
  }
}
