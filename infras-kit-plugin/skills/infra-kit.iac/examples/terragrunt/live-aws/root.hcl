remote_state {
  backend = "local"
  config = {
    path = "${get_parent_terragrunt_dir()}/state/${path_relative_to_include()}/terraform.tfstate"
  }
}

generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
terraform {
  required_version = ">= 1.6.0, < 2.0.0"
}
EOF
}
