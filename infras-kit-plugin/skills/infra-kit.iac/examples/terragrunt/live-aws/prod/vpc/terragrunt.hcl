include "root" {
  path = find_in_parent_folders("root.hcl")
}

locals {
  env = read_terragrunt_config(find_in_parent_folders("env.hcl"))
}

terraform {
  source = "../../../modules/vpc"
}

inputs = {
  project_name = local.env.locals.project
  environment  = local.env.locals.environment
  owner        = local.env.locals.owner
}
